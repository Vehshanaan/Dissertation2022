from setuptools import setup

package_name = 'prototype'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='vehshanaan',
    maintainer_email='vehshanaan@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [

            "NodeInstance = prototype.node:main",
            # ros2 run pkg 指令名 = 包名。对应python文件去掉py结尾：main
            "OOPNode = prototype.node_oop:main",
            "Talker = prototype.talker:main",
            "Listener = prototype.listener:main",
            "customMsg = prototype.customMsg:main",
            "customServer = prototype.customServer:main",
            "customClient = prototype.customClient:main",
            "parameter = prototype.parameters:main",
            "customActionServer = prototype.customActionServer:main",
            "customActionClient = prototype.customActionClient:main",
        ],
    },
)
