df['Helpful %'] = np.where(df['helpful_votes'] > 0,
                df['helpful_votes'] / df['total_votes'], -1)
df['% Upvote'] = pd.cut(df['Helpful %'],
        bins = [-1, 0, 0.2, 0.4, 0.6, 0.8, 1.0],
        labels = ['Empty', '0-20%', '20-40%',
		'40-60%', '60-80%', '80-100%']
                    , include_lowest = True)
df.head()
df_s = df.groupby(['star_rating', '% Upvote'])
		.agg({'review_id': 'count'})
df_s = df_s.unstack()
df_s.columns = df_s.columns.get_level_values(1)
fig = plt.figure(figsize=(15,10))
sns.heatmap(df_s[df_s.columns[::-1]].T,
            cmap = 'YlGnBu', linewidths=.5, annot = True)
plt.yticks(rotation=0)
plt.title('How helpful users find among user scores')
plt.show()
