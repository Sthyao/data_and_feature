# data_and_feature
Record some common characteristic engineering operations

1st:
The first work is statistical product for salesdate weight by month.

At the begging, we have sale data like this format:
date    name    amount
20xx-01 Sim     100
20xx-04 Sim     200
...

Now we want get [SALE_WRIGHT_MONTHLY]. We know that sales of products are always cyclical by time, in general, we use moving time averages to deal with problems like this. But we have a new idea to get the sale_wright to describe monthly sales trend of the product from history data.

Mean_month/Total_month\n
where Mean_month is mean of sale amount on year-on-year basis,
and Total_month is the average of the sum of historical sales data

This work solved several problems:
1.Data supplement and sorted by month
2.Data aggregate by month 
3.For different sale levels
The project cound be find in FILE Monthly_sales_weight
