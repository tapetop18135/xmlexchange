from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers

def index(request):
    data = """
    <data>
        <country name="Liechtenstein">
            <rank>1</rank>
            <year>2008</year>
            <gdppc>141100</gdppc>
            <neighbor name="Austria" direction="E"/>
            <neighbor name="Switzerland" direction="W"/>
        </country>
        <country name="Singapore">
            <rank>4</rank>
            <year>2011</year>
            <gdppc>59900</gdppc>
            <neighbor name="Malaysia" direction="N"/>
        </country>
        <country name="Panama">
            <rank>68</rank>
            <year>2011</year>
            <gdppc>13600</gdppc>
            <neighbor name="Costa Rica" direction="W"/>
            <neighbor name="Colombia" direction="E"/>
        </country>
    </data>
    """
    return HttpResponse(data, content_type='application/xml')

def calulator(x,y):
    return x+y

def cal(request, x,y):
    result = f"""
    <result>
        <r>{calulator(x,y)}</r>
    </result>
    """
    return HttpResponse(result, content_type='application/xml')