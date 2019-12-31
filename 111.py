from pyhdfs import HdfsClient
import pandas as pd

client = HdfsClient(hosts="172.16.18.114:50070,172.16.18.112:50070",user_name='hadoop')

path = 'hdfs://172.16.18.112:50070/a3bd481c98f44dde842367b7ebaef4a6/dataSet/vbap8482a43e3883413f8345344efa6b53ec/data/Data.csv'
head = client.open(path)
data = pd.read_csv(head)
print(data)