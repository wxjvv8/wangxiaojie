# 执行用例并生成html结果显示
### 执行所有用例并指定生成结果在report目录下：
pytest --alluredir ./report
### 启动allure serve生成html结果显示：
allure serve ./report
### 执行用例并清空历史数据：
pytest --alluredir ./report --clean-alluredir 
### 指定固定端口生成测试报告
allure serve ./report -p 8086
