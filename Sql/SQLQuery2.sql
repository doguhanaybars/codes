﻿Select * from Products

Select * from Products where ProductName like 'ch%'

Select * from Products where ProductName like '%a'

Select * from Products where ProductName like '%ch%'

Select * from Products where UnitPrice between 10 and 50 Order by UnitPrice desc

Select * from Products where CategoryID in (1,2) order by CategoryID

Select Count(*) as [Ürün Sayısı] from Products

Select Count(ProductName) from Products

Select Count(Region) from Customers

Select Min(UnitPrice) from Products
Select Max(UnitPrice) from Products
Select Avg(UnitPrice) from Products --ORTALAMA
Select Sum(UnitPrice * Quantity) as Kazanç from [Order Details]
Select Rand()








