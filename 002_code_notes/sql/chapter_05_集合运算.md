## 第五章 集合运算


集合在数学领域表示“各种各样的事物的总和”, 在数据库领域表示记录的集合. 具体来说,表、视图和查询的执行结果都是记录的集合, 其中的元素为表或者查询结果中的每一行。

在标准 SQL 中, 分别对检索结果使用 UNION, INTERSECT, EXCEPT 来将检索结果进行并,交和差运算, 像UNION,INTERSECT, EXCEPT这种用来进行集合运算的运算符称为集合运算符。

![jupyter](https://oss.linklearner.com/wonderful-sql/ch04/ch04.02.png)


### 1.表的加法(UNION)

#### 1.1 基本用法

![jupyter](https://oss.linklearner.com/wonderful-sql/ch04/ch04.03union.png)


求上图表的并集
```sql
select prodict_id,product_name
from product
union
select prodict_id,product_name
from product2

```
#### 1.2 OR与UNION的联系与区别:

对于同一个表的两个不同的筛选结果集, 使用 UNION 对两个结果集取并集, 和把两个子查询的筛选条件用 OR 谓词连接, 会得到相同的结果, 但倘若要将两个不同的表中的结果合并在一起, 就不得不使用 UNION 了。

即便是对于同一张表, 有时也会出于查询效率方面的因素来使用 UNION。

分别使用 UNION 或者 OR 谓词,找出成本利润率不足 30%或成本利润率未知的商品。

```sql
-- 使用 OR 谓词
SELECT * 
  FROM Product 
 WHERE sale_price / purchase_price < 1.3 
    OR sale_price / purchase_price IS NULL;
    
-- 使用 UNION
SELECT * 
  FROM Product 
 WHERE sale_price / purchase_price < 1.3
 
 UNION
SELECT * 
  FROM Product 
 WHERE sale_price / purchase_price IS NULL;
 
 ```
 
#### 1.3 不去重 UNION ALL

SQL 语句的 UNION 会对两个查询的结果集进行合并和去重, 这种去重不仅会去掉两个结果集相互重复的, 还会去掉一个结果集中的重复行. 但在实践中有时候需要需要不去重的并集, 在 UNION 的结果中保留重复行的语法其实非常简单,只需要在 UNION 后面添加 ALL 关键字就可以

```sql
-- 保留重复行
SELECT product_type
  FROM Product
 UNION ALL
SELECT product_type
  FROM Product2;
```

#### 1.4 隐式数据类型转换

1.通常来说会把类型完全一致并且代表相同属性的列使用 UNION 合并到一起显示      
2.但有时候, 即使**数据类型不完全相同, 也会通过隐式类型转换来将两个类型不同的列放在一列里显示**, 例如字符串和数值类型:

```sql
SELECT product_id, product_name, '1'
  FROM Product
 UNION
SELECT product_id, product_name,sale_price
  FROM Product2;
```
 

### 2.集合交运算不支持【INTERSECT】需要使用【 inner join 】来实现

集合的交, 就是两个集合的公共部分, 由于集合元素的互异性, 集合的交只需通过文氏图就可以很直观地看到它的意义。

```sql
SELECT p1.product_id, p1.product_name
  FROM Product p1
INNER JOIN Product2 p2
ON p1.product_id=p2.product_id
```

### 3.集合的减法不支持【EXCEPT】需要使用【NOT IN 谓词】来实现

求集合差集的减法运算和实数的减法运算有些不同,集合A和B做减法【A-B】只是将集合A中也同时属于集合B的元素减掉。

```sql
-- 使用 NOT IN 子句的实现方法
SELECT * 
  FROM Product
 WHERE product_id NOT IN (SELECT product_id 
                            FROM Product2)
```

### 4.对称差
两个集合A,B的对称差是指那些仅属于A或仅属于B的元素构成的集合。               
从直观上就能看出来, 两个集合的对称差等于 A-B并上B-A。         

```sql
-- 使用 NOT IN 实现两个表的差集
-- Product - Product2
SELECT * 
  FROM Product
 WHERE product_id NOT IN (SELECT product_id FROM Product2)
 
UNION

--  Product2 - Product
SELECT * 
  FROM Product2
 WHERE product_id NOT IN (SELECT product_id FROM Product)
```

### 5.连接

集合运算的特征就是以行方向为单位进行操作。  
通俗地说, 就是进行这些集合运算时, 会导致记录行数的增减。   
使用 UNION 会增加记录行数,而使用 INTERSECT 或者 EXCEPT 会减少记录行数。   

但这些运算不能改变列的变化, 虽然使用函数或者 CASE表达式等列运算, 可以增加列的数量, 但仍然只能从一张表中提供的基础信息列中获得一些"引申列", 本质上并不能提供更多的信息. 如果想要从多个表获取信息, 例如, 如果我们想要找出某个商店里的衣服类商品的名称,数量及价格等信息, 则必须分别从 ShopProduct 表和 Product 表获取信息。   

![jupyter](./images/chapter_05/sql-join.png)


#### 5.1 内连结(INNER JOIN)

```sql
-- 内连结
FROM <tb_1> INNER JOIN <tb_2> ON <condition(s)>
-- 示例
ELECT SP.shop_id
       ,SP.shop_name
       ,SP.product_id
       ,P.product_name
       ,P.product_type
       ,P.sale_price
       ,SP.quantity
  FROM ShopProduct AS SP
 INNER JOIN Product AS P
    ON SP.product_id = P.product_id;

```

关于内连结,需要注意以下三点:

**要点一: 进行连结时需要在 FROM 子句中使用多张表**

之前的 FROM 子句中只有一张表, 而这次同时使用了 ShopProduct 和 Product 两张表,使用关键字 INNER JOIN 就可以将两张表连结在一起:
> FROM ShopProduct AS SP INNER JOIN Product AS P

**要点二:必须使用 ON 子句来指定连结条件**

在进行内连结时 ON 子句是必不可少的,ON 子句是专门用来指定连结条件的, 在上述查询的 ON 之后指定两张表连结所使用的列以及比较条件, 基本上它能起到与 WHERE 相同的筛选作用。

**要点三: SELECT 子句中的列最好按照 表名.列名 的格式来使用。**

当两张表的列除了用于关联的列之外, 没有名称相同的列的时候, 也可以不写表名, 但表名使得我们能够在今后的任何时间阅读查询代码的时候, 都能马上看出每一列来自于哪张表, 能够节省我们很多时间。

```sql
SELECT  SP.shop_id,
        SP.shop_name,
        P.product_name
  FROM ShopProduct AS SP
 INNER JOIN Product AS P
    ON SP.product_id = P.product_id
 WHERE SP.shop_name = '东京'
   AND P.product_type = '衣服' ;
```
上述查询的执行顺序: `FROM 子句->WHERE 子句->SELECT 子句`

但是上述写法不建议大家使用,建议使用：
```sql
SELECT SP.shop_id,
       SP.shop_name,
       SP.product_id,
       P.product_name
  -- 子查询 1:从 ShopProduct 表筛选出东京商店的信息
  FROM (SELECT * FROM ShopProduct WHERE shop_name = '东京' ) AS SP
 INNER JOIN 
  -- 子查询 2:从 Product 表筛选出衣服类商品的信息
         (SELECT * FROM Product WHERE product_type = '衣服') AS P
    ON SP.product_id = P.product_id;
```

#### 5.2 外连结(OUTER JOIN)

内连结会丢弃两张表中不满足 ON 条件的行,和内连结相对的就是外连结. 外连结会根据外连结的种类有选择地保留无法匹配到的行。

按照保留的行位于哪张表,外连结有三种形式: **左连结, 右连结和全外连结**。

```sql
-- 左连结     
FROM <tb_1> LEFT  OUTER JOIN <tb_2> ON <condition(s)>
-- 右连结     
FROM <tb_1> RIGHT OUTER JOIN <tb_2> ON <condition(s)>
-- 全外连结【mysql 使用 UNION 实现全连结】
FROM <tb_1> FULL  OUTER JOIN <tb_2> ON <condition(s)>
```



