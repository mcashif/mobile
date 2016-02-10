from tastypie.resources import ModelResource
from directme.models import DriverJob,Client, Driver
from tastypie.authorization import Authorization
from tastypie import fields
from tastypie.authorization import DjangoAuthorization
from tastypie.resources import ModelResource, ALL, ALL_WITH_RELATIONS
from tastypie.serializers import Serializer



class DriverResource(ModelResource):

    class Meta:
        queryset = Driver.objects.all()
        resource_name = 'driver'
        authorization = Authorization()

class ClientRecorce(ModelResource):

    class Meta:
        queryset = Client.objects.all()
        resource_name = 'client'
        authorization = Authorization()

class DriverJobResource(ModelResource):

    clientid = fields.ForeignKey(ClientRecorce, 'clientid',full=True)
    driverid = fields.ForeignKey(DriverResource, 'driverid',full=True)


    class Meta:
        queryset = DriverJob.objects.all()
        resource_name = 'driverjob'
        list_allowed_methods = ['get', 'post']
        detail_allowed_methods = ['get', 'post', 'put', 'delete']
        authorization = Authorization()
        filtering = {
            'driverid': ALL_WITH_RELATIONS,
            'isdelivered': ALL,
            'created': ['exact', 'range', 'gt', 'gte', 'lt', 'lte'],
        }
        serializer = Serializer()
