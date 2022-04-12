# data_and_feature
Record some common characteristic engineering operations<br />

##1st:<br />
The first work is statistical product for salesdate weight by month.<br />

At the begging, we have sale data like this format:<br />
date    name    amount<br />
20xx-01 Sim     100<br />
20xx-04 Sim     200<br />
...

Now we want get **[SALE_WRIGHT_MONTHLY]**. <br />We know that sales of products are always cyclical by time, in general, we use moving time averages to deal with problems like this. But we have a new idea to get the sale_wright to describe monthly sales trend of the product from history data.<br />

Mean_month/Total_month<br />
where Mean_month is mean of sale amount on year-on-year basis,\
and Total_month is the average of the sum of historical sales data<br />

This work solved several problems:<br />
1.Data supplement and sorted by month<br />
2.Data aggregate by month <br />
3.For different sale levels<br />
The project cound be find in FILE Monthly_sales_weight<br />
