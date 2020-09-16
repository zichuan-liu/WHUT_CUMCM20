import itertools
 
class Apriori(object):
    
    def __init__(self,min_sup=0.2,dataDic={}):
        self.data = dataDic      #构建数据记录词典
        self.size = len(dataDic) #统计事务个数
        self.min_sup = min_sup   #最小支持度阈值
        self.min_sup_val = min_sup * self.size  #最小支持度计数
 
    def find_frequent_1_itemsets(self):
        FreqDic = {}   #用于统计物品的支持度计数
        for event in self.data:    #event为每一条记录
            for item in self.data[event]:   #item为项
                if item in FreqDic:
                    FreqDic[item] += 1
                else:
                    FreqDic[item] = 1
 
        L1 = []
        for itemset in FreqDic:
            if FreqDic[itemset] >=self.min_sup_val:  #过滤掉小于最小支持度计数的1-项集
                L1.append([itemset])
        return L1
 
    def has_infrequent_subset(self,c,L_last,k):
        #c为当前集合，L_last为上一个频繁项集的集合，k为当前频繁项集内的元素个数
        #该函数用于检查当前子集是否都为频繁项集
        subsets = list(itertools.combinations(c,k-1))
        for each in subsets:
            each = list(each)
            if each not in L_last:
                return True
        return False
 
    def apriori_gen(self,L_last):  #连接步实现
        k = len(L_last[0]) + 1
        Ck = []
        for itemset1 in L_last:
            for itemset2 in L_last:
                flag = 0
                for i in range(k-2):
                    if itemset1[i] != itemset2[i]:    #如果前k-2项中有一项不相等，则合并的项集必定不为频繁项集
                        flag = 1
                        break
                if flag == 1:continue
                if itemset1[k-2] < itemset2[k-2]:
                    c = itemset1 + [itemset2[k-2]]    #合成待定k项集
                else:
                    continue
 
                if self.has_infrequent_subset(c,L_last,k):  #判断是否为1-项集
                    continue
                else:
                    Ck.append(c)
        return Ck
 
    def do(self):
        L_last = self.find_frequent_1_itemsets()   #找到频繁一项集
        L = L_last
        i = 0
        while L_last != []:
            Ck = self.apriori_gen(L_last) 
            FreqDic = {}        
            for event in self.data:
                for c in Ck:    
                    if set(c) <= set(self.data[event]):
                        if tuple(c) in FreqDic:
                            FreqDic[tuple(c)] += 1
                        else:
                            FreqDic[tuple(c)] = 1
            Lk = []
            for c in FreqDic:
                if FreqDic[c] > self.min_sup_val: 
                    Lk.append(list(c))
            L_last = Lk
            L += Lk
        return L
 