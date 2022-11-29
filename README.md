# Avenga Internship task

Here is a dataset: "https://www.kaggle.com/datasets/anandaramg/taxi-trip-data-nyc?resource=download". 
Using Apache Spark (Scala or Python), get the following report:
|-- Vendor: string (nullable = true) - name of vendor
|-- Payment Type: string (nullable = true) - name of payment type
|-- Payment Rate: double (nullable = true) - payment_total / passengers count per vendor and payment type
|-- Next Payment Rate: double (nullable = true) - next record(bigger) payment rate for vendor
|-- Max Payment Rate: double (nullable = true) - max payment rate for vendor
|-- Percents to next rate: string (nullable = true) - how many points (in percents) is necessary to achieve the next record payment rate

Gather your results in json or csv and send via python/scala function to avenga.academy@avenga.com. Additionally, send an explanation of
your solution and link on GitHub.
