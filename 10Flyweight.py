#!/usr/bin/python
#coding=utf-8
#desc:10.享元模式，Flyweight Pattern
#TP demo


#region ConcreteFlyweight 具体享元类

class ComplexGenetics(object):
    def __init__(self):
        pass
    
    def genes(self, gene_code):
        return "Complex Patter[%s]Too huge in Size" % (gene_code)


#endregion



#region FlyweightFactory 字典控制享元

class Families(object):
    family = {}

    def __new__(cls, name, family_id):
        try:
            id = cls.family[family_id]
        except KeyError:
            id = object.__new__(cls)
            cls.family[family_id] = id
        return id

    def set_genetic_info(self, genetic_info):
        cg = ComplexGenetics()
        self.genetic_info = cg.genes(genetic_info)

    def get_genetic_info(self):
        return self.genetic_info


#endregion



def test():
    data = (('a', 1, 'ATAG'), ('a', 2, 'AAGT'), ('b', 1, 'ATAG'))
    family_objs = []
    for i in data:
        obj = Families(i[0], i[1])
        obj.set_genetic_info(i[2])
        family_objs.append(obj)

    for i in family_objs:
        print ("id=" + str(id(i)))
        print (i.get_genetic_info())

    print("相同id说明使用了同一个实例，节省了内存开销")

if __name__ == "__main__":
    print("Start!")

    test()

    print("Done!")