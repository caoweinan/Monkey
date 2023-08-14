# -*- coding: utf-8 -*-


class MonkeyConfig(object):
    # 测试的app包名
    # package_name = "com.sdpopen.demo"
    package_name = "com.mymoney"

    # 测试app中模块的关键词
    # module_key = "com.sdpopen.wallet"
    module_key = "com.mymoney"

    # todo 自动找到apk中exported的activity
    # 卡死状态随机跳转的activity,第一个元素为测试初始页
    activity = ["com.mymoney/.biz.main.MainActivity",
                "com.mymoney/.biz.navtrans.activity.NavYearTransActivity",
                "com.mymoney/.biz.basicdatamanagement.biz.account.activity.AccountActivity",
                "com.mymoney/.loan.biz.activity.MyCashNowMainActivity",
                "com.mymoney/.biz.finance.FinanceActivity",
                "com.mymoney/.biz.setting.SettingActivity",
                "com.mymoney/.biz.addtrans.activity.AddTransActivity",
                "com.mymoney/.biz.main.bottomboard.SettingBottomBoardActivity"]

    monkeyCmd = f"monkey -p {package_name} --throttle 300  " \
                "--pct-appswitch 5 --pct-touch 30 --pct-motion 60 --pct-anyevent 5  " \
                "--ignore-timeouts --ignore-crashes   --monitor-native-crashes -v -v -v 300 > "
