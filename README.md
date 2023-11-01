# FullStackDemo
Full Stack Demo Tutorial


## 前端

1. 下载安装npm（前端必备软件管理工具）
    
    `npm`（Node Package Manager）是一个基于Node.js的包管理工具，主要用于JavaScript编程语言的包管理。它是全球最大的软件注册中心，包含了超过800,000个代码包，每星期大约有30亿次的下载量。
    
2. 创建一个vue项目
    
    ```bash
    npm install -g vue-cli
    
    vue init webpack projec_name
    
    npm install axios -S
    npm i element-ui -S
    ```
    
    vue-cli: vue脚手架工具
    
    axios: 访问后端api工具
    
    element-ui: 后端UI工具
    
3. 在main.js文件中加入
    
    ```jsx
    import "element-ui/lib/theme-chalk/index.css";
    import axios from "axios";
    
    Vue.use(ElementUI);
    ```
    
4. 在vue文件中写一个接口连到后端
    
    这部分主要写到js部分，示例代码：
    
    data部分是当前页面所需的所有变量，methods部分是所有函数方法，如果需要在函数中调用data中的变量，需要指定this。
    
    ```jsx
    <script>
    import axios from "axios";
    export default {
      name: 'HelloWorld',
      data () {
        return {
          msg: 'Welcome to Your Vue.js App',
          tableData: [],
        }
      },
    
      methods: {
        fetch_paper() {
          const limit=8
          const param = `num=${limit}`;
          // 在这里调接口
          axios
            .get(`http://127.0.0.1:8000/paper?${param}`)
            .then((res) => {
              this.tableData = res.data.data;
              this.time = res.data.time;
              console.log(this.tableData, this.time);
            })
            .catch(() => {
              this.$notify({title: "Error", message: "Please try again!", type: "error",});
            });
    
        },
      }
    }
    </script>
    ```
    
5. 测试环境中运行
    
    ```bash
    npm run dev
    ```
    

更多内容参考：[https://www.omegaxyz.com/2020/11/30/vue-manual/](https://www.omegaxyz.com/2020/11/30/vue-manual/)

## 后端

1. 安装Python包
    
    利用fastapi作为快速的后端部署，如果需要连接数据库，则使用pymysql，如果数据库操作比较多，建议使用aiomysql来异步操作数据库。
    
    ```bash
    pip install fastapi
    pip install uvicorn
    pip install pymysql
    ```
    
2. 示例代码：
    
    ```python
    import uvicorn
    from fastapi import FastAPI, Query, Form, APIRouter, File, UploadFile
    from fastapi.middleware.cors import CORSMiddleware
    import time
    
    app = FastAPI(
        title="demo",
        docs_url='/api/v1/docs',
        redoc_url='/api/v1/redoc',
        openapi_url='/api/v1/openapi.json'
    )
    
    router = APIRouter()
    
    @router.get('/paper')
    async def fetch_paper(
        num: int = Query(..., description='returned paper num', example='10')
    ):
        start = time.time()
        print(num)
        return {'time': time.time() - start, 'data': num}
    
    @router.post('/add_paper')
    async def add_paper(
            name: str = Form(..., description='paper name', example='Attention is all you need'),
            info: str = Form(..., description='paper info', example='NIPS 2017')
    ):
        start = time.time()
        print(name, info)
        return {'time': time.time() - start}
    
    @router.put('/update_paper')
    async def update_paper(
            p_id: str = Form(..., description='paper id', example='1234'),
    ):
        start = time.time()
        print(p_id)
        return {'time': time.time() - start}
    
    @router.delete('/delete_paper')
    async def delete_paper(
            p_id: str = Query(..., description='paper is', example='1234')
    ):
        start = time.time()
        print(p_id)
        return {'time': time.time() - start}
    
    app.include_router(router)
    
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    
    if __name__ == '__main__':
        uvicorn.run(app=app, host="127.0.0.1", port=8000, workers=1)
    ```
    
3. 启动程序
    
    ```bash
    python apiCore.py
    ```
    
    或
    
    ```bash
    uvicorn apiCore:app --reload --port 9918 --host 0.0.0.0
    ```
    
4. 接口调试
    
    可以采用fastapi自带的一个前端接口进行调试
    
    进入http://127.0.0.1:8000/api/v1/docs页面调试
    
    更多内容参考：[https://www.omegaxyz.com/2020/08/18/restful-fastapi/?highlight=fastapi](https://www.omegaxyz.com/2020/08/18/restful-fastapi/?highlight=fastapi)
    

## 数据库

1. 下载并安装MySQL数据库以及数据库管理工具，建议使用navicat
2. 在MySQL中导入数据
    
    这里可以使用示例数据paper_db.sql（包含少量的paper信息），直接用navicat导入这个库即可（需要在你创建的数据库下）
    
3. 后端链接数据库并在数据库中操作（这里的示例是从数据库中取数据）
    
    ```python
    import pymysql
    
    # 连接配置信息
    config = {
        'host': 'localhost',
        'port': 3306,  # MySQL默认端口
        'user': 'root',  # mysql默认用户名
        'password': '12345678',
        'db': 'paper_db',  # 数据库
        'charset': 'utf8mb4',
        'cursorclass': pymysql.cursors.DictCursor,
    }
    
    def db_get_paper(num=10):
    		# am_paper为paper_db中的一个表
        try:
            con = pymysql.connect(**config)
            sql = "SELECT * FROM am_paper limit %d" % num
            with con.cursor() as cursor:
                cursor.execute(sql)
                result = cursor.fetchall()
                con.close()
            return result
        except Exception as e:
            print(e)
            return []
    ```