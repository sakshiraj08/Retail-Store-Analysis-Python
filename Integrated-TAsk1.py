#!/usr/bin/env python
# coding: utf-8

# In[82]:


import pandas as pd
import numpy as np
import os
os.chdir('C:\\Users\\user\\Music')
order=pd.read_csv('Orders.csv')
order.head()


# In[27]:


customer=pd.read_csv('Customer.csv')
customer.head()


# In[86]:


order_cust=pd.merge(order,customer)
order_cust


# In[28]:


#Q1. Total Revenue (order value)


# In[29]:


Total_Revenue=order['ORDER_TOTAL'].sum()
Total_Revenue


# In[30]:


#Q2. Total Revenue (order value) by top 25 Customers


# In[31]:


Total_Revenue_top=order['ORDER_TOTAL'].sort_values(ascending=False).head(25)
Total_Revenue_top


# In[32]:


#Q3. Total number of orders


# In[33]:


Total_number_orders=order['ORDER_NUMBER'].count()
Total_number_orders


# In[34]:


#Q4. Total orders by top 10 customers


# In[35]:


Total_number_orders_10=order['ORDER_NUMBER'].sort_values(ascending=False).head(10)
Total_number_orders_10


# In[36]:


#Q6. Number of customers ordered once


# In[37]:


customer_ordered=order['CUSTOMER_KEY'].value_counts()
customer_ordered_once=customer_ordered[customer_ordered==1]
total=len(customer_ordered_once)
total


# In[38]:


#Q7. Number of customers ordered multiple times


# In[39]:


customer_ordered1=order['CUSTOMER_KEY'].value_counts()


# In[40]:


customer_ordered_multiple=customer_ordered1[customer_ordered1>1]


# In[41]:


total1=len(customer_ordered_multiple)
total1


# In[42]:


#Q8. Number of customers reffered to other customers


# In[43]:


number_of_customers=customer['Referred Other customers'].nunique()
number_of_customers


# In[44]:


#Q9. Which Month have maximum Revenue?


# In[45]:


import datetime
order['ORDER_DATE']=pd.to_datetime(order['ORDER_DATE'])
order["ORDER_MONTH"]=order['ORDER_DATE'].dt.month

maximum_revenue=order.groupby('ORDER_MONTH')['ORDER_TOTAL'].sum()
maximum_revenue


# In[46]:


#Q10. Number of customers are inactive (that haven't ordered in the last 60 days)


# In[47]:


from datetime import datetime,timedelta
order['ORDER_DATE']=pd.to_datetime(order['ORDER_DATE'])
current_date=datetime.today()
cutoff=current_date-timedelta(days=60)
customers_number=order.groupby('ORDER_NUMBER')['ORDER_DATE'].max()
inactive_customer=customers_number[customers_number<cutoff]
count=len(inactive_customer)
count


# In[48]:


#Q11. Growth Rate  (%) in Orders (from Nov’15 to July’16)


# In[49]:


order_2015=order['ORDER_DATE'<='2015-11-01']&['ORDER_DATE'<'2015-07-16']
order_2016=order['ORDER_DATE'<='2016-11-01']&['ORDER_DATE'<'2016-07-16']
count1=len(order_2015)
count2=len(order_2016)
growth_rate=(count1-count2/count1)*100
growth_rate


# In[50]:


#Q12. Growth Rate (%) in Revenue (from Nov'15 to July'16)


# In[51]:


#Q13. What is the percentage of Male customers exists?


# In[52]:


num_male=(customer['Gender']=='M').sum()
length=len(customer.CUSTOMER_KEY)


# In[53]:


num_male


# In[54]:


#Q14. Which location have maximum customers?


# In[66]:


max_cust=customer[['CUSTOMER_KEY','Location']].groupby('Location')['CUSTOMER_KEY'].count().sort_values(ascending=False)


# In[67]:


max_cust


# In[ ]:


#Q15. How many orders are returned? (Returns can be found if the order total value is negative value)


# In[83]:


negative_value=[order['ORDER_TOTAL']<0]
retured_order=len(negative_value)
retured_order


# In[ ]:


#Q16. Which Acquisition channel is more efficient in terms of customer acquisition?


# In[96]:


number_acq=order_cust[['ORDER_TOTAL','Acquired Channel']].groupby('Acquired Channel')['ORDER_TOTAL'].sum()
number_acq


# In[92]:


number_customer=customer[['CUSTOMER_KEY','Acquired Channel']].groupby('Acquired Channel')['CUSTOMER_KEY'].count()


# In[93]:


number_customer


# In[97]:


efficient=number_acq/number_customer


# In[98]:


efficient


# In[ ]:


#Q17. Which location having more orders with discount amount?


# In[109]:


sum_discount=order_cust[['DISCOUNT','Location']].groupby('Location')['DISCOUNT'].sum().sort_values(ascending=False)
sum_discount


# In[ ]:


#Q18. Which location having maximum orders delivered in delay?


# In[112]:


delivered_delay=order_cust[['DELIVERY_STATUS','Location']].groupby('Location')['DELIVERY_STATUS'].count().sort_values(ascending=False)
delivered_delay


# In[ ]:


#Q19. What is the percentage of customers who are males acquired by APP channel?


# In[124]:


APP_count=order_cust['Acquired Channel']=='AAP'
count_1=len(APP_count)
Gender_count=order_cust['Gender']=='M'
count_male=len(Gender_count)
percentage=(count_male/count_1)*100
percentage


# In[ ]:


#Q20. What is the percentage of orders got canceled?


# In[142]:


total_order_status=order['ORDER_STATUS']
count_total=len(total_order_status)
order_cancelled=order['ORDER_STATUS']=='Cancelled'
count_2=len(order_cancelled)
percentage1=(count_2/count_total)*100
percentage1


# In[ ]:


#Q21. What is the percentage of orders done by happy customers 
#(Note: Happy customers mean customer who referred other customers)?


# In[144]:


total_order_status=customer['Referred Other customers']
count_total=len(total_order_status)
order_cancelled=customer['Referred Other customers']=='Y'
count_2=len(order_cancelled)
percentage1=(count_2/count_total)*100
percentage1


# In[150]:


#Q22. Which Location having maximum customers through reference?
referred_customers = order_cust[order_cust['Referred Other customers'].notnull()]

customers_by_location = referred_customers.groupby('Location')['CUSTOMER_KEY'].count().idxmax()

print("Location with Maximum Customers through Reference:", customers_by_location)


# In[ ]:


#Q23. What is order_total value of male customers who are belongs to Chennai and Happy customers (Happy customer definition is same in question 21)?


# In[151]:


happy_male_chennai_orders = order_cust[
    (order_cust['CUSTOMER_KEY'].isin(customer[(customer['Gender'] == 'M') & 
                                          (customer['Location'] == 'Chennai') & 
                                          (customer['Referred Other customers'].notnull())]['CUSTOMER_KEY']))]

order_total_value = happy_male_chennai_orders['ORDER_TOTAL'].sum()

print(f"The order_total value of male customers who are from Chennai and have referred other customers is:\
{order_total_value}")


# In[ ]:


#Q24. Which month having maximum order value from male customers belongs to Chennai?


# In[154]:


from datetime import datetime
chennai_male_data = order_cust[(order_cust['Gender'] == 'M') & (order_cust['Location'] == 'Chennai')]

monthly_order_totals = chennai_male_data.groupby(chennai_male_data['ORDER_DATE'].dt.month)['ORDER_TOTAL'].sum()

max_month = monthly_order_totals.idxmax()

print(f"The month with the maximum order value from male customers in Chennai is {max_month}.")


# In[ ]:





# In[ ]:


#Q25. What are number of discounted orders ordered by female customers who were acquired by website from Bangalore and delivered orders  on time?


# In[155]:


discounted_orders = order_cust[(order_cust['DISCOUNT'] > 0) & 
                                (order_cust['Gender'] == 'F') & 
                                (order_cust['Acquired Channel'] == 'WEBSITE') & 
                                (order_cust['Location'] == 'Bangalore') & 
                                (order_cust['DELIVERY_STATUS'] == 'ON-TIME')]

num_discounted_orders = discounted_orders.shape[0]

print(f"The number of discounted orders ordered by female customers who were acquired by the \
website from Bangalore and had their orders delivered on time is: {num_discounted_orders}")


# In[ ]:




