# coding: utf-8
import unittest
import requests
from hypothesis import given,settings, strategies as st

test_number = 0

class TestWeatherStackAPI(unittest.TestCase):
    
    @settings(deadline=None, max_examples=2)
    @given(
        origin_longitude=st.floats(min_value=116.0,max_value=117.0),  # origin
        origin_latitude=st.floats(min_value=39.0,max_value=40.0),
        destination_longitude=st.floats(min_value=116.0,max_value=117.0),  # destination
        destination_latitude=st.floats(min_value=39.0,max_value=40.0)
    )
    
    def test_get_walking_route(self,origin_longitude,origin_latitude,destination_longitude,destination_latitude):
        # 设置API端点和查询参数
        base_url = "https://restapi.amap.com/v3/direction/walking"
        query_params = {
            "origin": str(origin_longitude)+','+str(origin_latitude),
            "destination": str(destination_longitude)+','+str(destination_latitude),
            "key": "your_key"
        }
        # 发送GET请求
        response = requests.get(base_url, query_params)
        # 验证HTTP响应码
        self.assertEqual(200, response.status_code)
        # 解析JSON响应
        json_response = response.json()
        # 验证JSON响应中的某些字段值
        global test_number
        test_number=test_number+1        
        print("test",test_number)
        print(json_response['route']['origin'])
        print(json_response['route']['destination'])
        print("\n")
        self.assertIn('status', json_response)
        self.assertIn('info', json_response)
        self.assertIn('infocode', json_response)
        self.assertIn('count',json_response)
        self.assertIn('route',json_response)

    def test_get_bus_route(self,origin_longitude,origin_latitude,destination_longitude,destination_latitude):
        # 设置API端点和查询参数
        base_url = "https://restapi.amap.com/v3/direction/transit/integrated"
        query_params = {
            "origin": str(origin_longitude)+','+str(origin_latitude),
            "destination": str(destination_longitude)+','+str(destination_latitude),
            "city": "010",
            "key": "your_key"
        }
        # 发送GET请求
        response = requests.get(base_url, query_params)
        # 验证HTTP响应码
        self.assertEqual(200, response.status_code)
        # 解析JSON响应
        json_response = response.json()
        # 验证JSON响应中的某些字段值
        global test_number
        test_number=test_number+1        
        print("test",test_number)
        print(json_response['city'])
        print(json_response['route']['origin'])
        print(json_response['route']['destination'])
        print("\n")
        self.assertIn('status', json_response)
        self.assertIn('info', json_response)
        self.assertIn('infocode', json_response)
        self.assertIn('count',json_response)
        self.assertIn('route',json_response)

    def test_get_driving_route(self,origin_longitude,origin_latitude,destination_longitude,destination_latitude):
        # 设置API端点和查询参数
        base_url = "https://restapi.amap.com/v3/direction/driving"
        query_params = {
            "origin": str(origin_longitude)+','+str(origin_latitude),
            "destination": str(destination_longitude)+','+str(destination_latitude),
            "key": "your_key"
        }
        # 发送GET请求
        response = requests.get(base_url, query_params)
        # 验证HTTP响应码
        self.assertEqual(200, response.status_code)
        # 解析JSON响应
        json_response = response.json()
        # 验证JSON响应中的某些字段值
        global test_number
        test_number=test_number+1        
        print("test",test_number)
        print(json_response['route']['origin'])
        print(json_response['route']['destination'])
        print("\n")
        self.assertIn('status', json_response)
        self.assertIn('info', json_response)
        self.assertIn('infocode', json_response)
        self.assertIn('count',json_response)
        self.assertIn('route',json_response)

    def test_get_bicycle_route(self,origin_longitude,origin_latitude,destination_longitude,destination_latitude):
        # 设置API端点和查询参数
        base_url = "https://restapi.amap.com/v4/direction/bicycling"
        query_params = {
            "origin": str(origin_longitude)+','+str(origin_latitude),
            "destination": str(destination_longitude)+','+str(destination_latitude),
            "key": "your_key"
        }
        # 发送GET请求
        response = requests.get(base_url, query_params)
        # 验证HTTP响应码
        self.assertEqual(200, response.status_code)
        # 解析JSON响应
        json_response = response.json()
        # 验证JSON响应中的某些字段值
        global test_number
        test_number=test_number+1        
        print("test",test_number)
        print(json_response['data']['origin'])
        print(json_response['data']['destination'])
        print("\n")
        self.assertIn('data', json_response)
        self.assertIn('errcode', json_response)
        self.assertIn('errmsg',json_response)
        self.assertIn('errdetail',json_response)



if __name__ == '__main__':
    unittest.main()