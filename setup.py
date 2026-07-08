from setuptools import setup
setup(
    name="vpnx",
    version="1.0.0",
    description="VPN Proxy Exchange",
    py_modules=["vpnx_cli"],
    entry_points={"console_scripts": ["vpnx=vpnx_cli:main"]},
    python_requires=">=3.8",
)
