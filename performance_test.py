from locust import HttpUser, task, between
from hypothesis import given, strategies as st

test_number = 0

class YourLocustUser(HttpUser):

    wait_time = between(1, 2)

    @task

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
        response = self.client.get(base_url, params=query_params)
        # 验证HTTP响应码
        self.assertEqual(200, response.status_code)
        # 解析JSON响应
        json_response = response.json()
        # 验证JSON响应中的某些字段值
        #print(json_response)
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

