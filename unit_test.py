# coding: utf-8
import unittest
import requests

test_number = 0

class TestWeatherStackAPI(unittest.TestCase):
    
    def test_get_walking_route(self):

        # 设置API端点和查询参数
        base_url = "https://restapi.amap.com/v3/direction/walking"
        query_params = {
            "origin": "116.481028,39.989643",
            "destination": "116.434446,39.90816",
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

    def test_get_bus_route(self):
        # 设置API端点和查询参数
        base_url = "https://restapi.amap.com/v3/direction/transit/integrated"
        query_params = {
            "origin": "116.481499,39.990475",
            "destination": "116.465063,39.999538",
            "city":"010",
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

    def test_get_driving_route(self):
        # 设置API端点和查询参数
        base_url = "https://restapi.amap.com/v3/direction/driving"
        query_params = {
            "origin": "116.481028,39.989643",
            "destination": "116.465302,40.004717",
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

    def test_get_bicycle_route(self):
        # 设置API端点和查询参数
        base_url = "https://restapi.amap.com/v4/direction/bicycling"
        query_params = {
            "origin": "116.481499,39.990475",
            "destination": "116.465063,39.999538",
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
        #print(json_response['data']['origin'])
        #print(json_response['data']['destination'])
        print(json_response)
        print("\n")
        self.assertIn('data', json_response)
        self.assertIn('errcode', json_response)
        self.assertIn('errmsg',json_response)
        self.assertIn('errdetail',json_response)



if __name__ == '__main__':
    unittest.main()