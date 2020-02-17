# -*- coding: utf-8 -*-


class MonkeyConfig(object):
    # 测试的app包名
    # package_name = "com.sdpopen.demo"
    package_name = "com.zxhd"

    # 测试app中模块的关键词
    # module_key = "com.sdpopen.wallet"
    module_key = "com.zxhd"

    # todo 自动找到apk中exported的activity
    # 卡死状态随机跳转的activity,第一个元素为测试初始页
    activity = ["com.zxhd/.view.main.activity.MainActivity",
                "com.zxhd/.view.home.activity.CourseListActivity",
                "com.zxhd/.view.person.activity.UserInfoFixActivity",
                "com.zxhd/.view.home.activity.CommonWebHActivity",
                "com.zxhd/.view.person.activity.UserCourseActivity",
                "com.zxhd/.view.person.activity.UserCandyActivity",
                "com.zxhd/.view.person.activity.SettingActivity"]

    monkeyCmd = f"monkey -p {package_name} --throttle 300  " \
                "--pct-appswitch 5 --pct-touch 30 --pct-motion 60 --pct-anyevent 5  " \
                "--ignore-timeouts --ignore-crashes   --monitor-native-crashes -v -v -v 300 > "
