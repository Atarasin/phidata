# GUIDER

## 1. 写在前面

1. 鉴于学习的目的，不要直接安装`phidata`库，而是拉取代码到本地，方便修改和测试。
2. 可以将`phidata`拉取路径添加到`PYTHONPATH`环境变量中，这样就可以在任何地方调用`phidata`库了。

## 2. phidata库的修改

1. 由于不是通过`pip`等路径正常安装，需要修改源码，才能使得`phidata`库能够正常运行。
    ```python
    class PhiCliSettings(BaseSettings):
    app_name: str = "phi"
    # app_version: str = metadata.version("phidata")
    app_version: str = "0.0.1"
    ```
2. 为了便于调试，修改日志模块的输出级别与格式。
    ```python
    logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(name)s %(levelname)s %(filename)s:%(funcName)s:%(lineno)d %(message)s')
    ```