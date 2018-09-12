import yaml
from threading import Thread
from time import sleep, time

from osisoft.pidevclub.piwebapi.models import PIAnalysis, PIItemsStreamValues, PIStreamValues, PITimedValue, PIPoint, \
    PIDataServer, PIElement, PIAttribute
from osisoft.pidevclub.piwebapi.pi_web_api_client import PIWebApiClient
from osisoft.pidevclub.piwebapi.rest import ApiException

class GetData():
    def getCredentials(self):
        conf = yaml.load(open('conf/credentials.yml'))
        url = conf['pi']['url']
        username = conf['pi']['username']
        pwd = conf['pi']['password']
        return url,username,pwd

    def getPIWebApiClient(self):
        """
            TODO: The PI Web API client must provide a user name and password when using “basic” authentication
            Store passwords outside of the code in a hardware TPM, trusted service (credential manager) or in a protected file.
            Code to return the user name and password is not shown here.
        """
        url, username, password = self.getCredentials()
        print ("url %s, username %s, password %s" % (url, username, password))
        return PIWebApiClient(
                        url, 
                        useKerberos=False, 
                        username=username, 
                        password=password, 
                        verifySsl=False)

    def CreatePIPoint(self):
        client = self.getPIWebApiClient()
        newPoint = PIPoint()
        newPoint.name  = "S1_PREL"
        newPoint.descriptor = "Sensor Relative Pression"
        newPoint.point_class = "classic"
        newPoint.point_type = "float32"
        newPoint.future = False
        dataServer = client.dataServer.get_by_path("\\\\PISRV1")
        return client.dataServer.create_point_with_http_info(dataServer.web_id, newPoint)      

    def GetDataInBulk(self):
        client = self.getPIWebApiClient()
        point1 = client.point.get_by_path("\\\\PISRV1\\sinusoid", None, None)
        point2 = client.point.get_by_path("\\\\PISRV1\\cdt158", None, None)
        point3 = client.point.get_by_path("\\\\PISRV1\\sinusoidu", None, None)

        webIds = list()
        webIds.append(point1.web_id)
        webIds.append(point2.web_id)
        webIds.append(point3.web_id)

        piItemsStreamValues = client.streamSet.get_recorded_ad_hoc(webIds, start_time="*-3d", end_time="*",
                                                                   include_filtered_values=True, max_count=1000)
        return piItemsStreamValues


g = GetData()
#g.CreatePIPoint()
print(g.GetDataInBulk())
