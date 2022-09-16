# 1024(草榴论坛)-Autoreply 多用户版本

购买草榴邀请码 [联系](https://t.me/honus_chat_bot)

ps: 多个账号只需要用空格隔开即可

**警告:使用过程建议多注意更新，否则可能草榴社区更改造成封号风险**

**#更新日志**

```
2022.09.15 修复草榴从http变更为https造成的登录失败
2022.6.30  增加点赞功能，每日只点击一次  
2022.4.19  增加免费验证码api地址，感谢 @l107868382
2021.12.21 修复草榴社区编码修改造成的错误
2021.3.14  通过添加config文件配置验证码手动输入，排除版主帖子
2021.2.22  增加多用户版本，切换分支查看
2021.2.6   修复草榴社区更改造成的链接移除失败。已修改为自动获取全部置顶链接
2021.1.22  修复草榴社区更改造成的回复失败
```

~~因为考研在即~~(考完了，体验了一次真题。体验很好，下次不来了)，加上1024的回复机制确实有点繁琐，所以打算用个python脚本做一个自动回帖，本脚本主要适用于新手上路到侠客之间

config配置。使用方法为:

```
config={
    'Forbid':  True,              #True为屏蔽版主发帖,无参数或者False为不屏蔽
    'Input_self':  False,         #设置为True为手动输入验证码,无参数或者False为自动输入
    'like': True,                 #True为每日自动点赞一次，无参数默认为True
}
```

<h4>使用说明(github Actions方式)</h4>

![Fork位置与Settings位置](https://fastly.jsdelivr.net/gh/0honus0/1024-Autoreply@Multi_User/doc/fork%20and%20settings.png)

![Secrets位置](https://fastly.jsdelivr.net/gh/0honus0/1024-Autoreply@Multi_User/doc/Secrets.png)

![new secret位置](https://fastly.jsdelivr.net/gh/0honus0/1024-Autoreply@Multi_User/doc/new%20Secret.png)

<h4>1.Fork之后，通过settings -> Secrets -> new secret添加下列值</h4>

(必需)

```
USER             用户名

PASSWORD         密码

SECRET           谷歌身份验证器密钥
```

(可选1)([申请地址](https://apitruecaptcha.org/))

```
USERID            api页面中的userid字段
APIKEY            api页面中的apikey字段
```

(可选2)([注册地址](http://ttshitu.com/register.html?inviter=3d92d1b2371f487d9072430a93bb043c) )

```
CODEUSER         注册用户名

CODEPASS         注册密码
```

ps:可选两个是识别验证码用的，任选其一即可，也可以都不选。如果不选碰见需要验证码的则会运行失败。

```
第一个是免费的api接口，每天100次免费的

第二个是自己找的一个平台，1元可以识别500次
```

想要更换验证方式的，修改1024.py 316行，324行为 `GetVerificationCode.`+getver中的函数名

<h4>
2.

(1)先点击Actions,同意使用协议。

(2)点击左侧树形图中的 `1024-AutoReply`,然后点击右边的 `Run workdlow` 即可手动触发执行一次。（后续除非是调试，否则等待自动执行就可以了）

(可选)3.可以通过 `getreply()中的reply`设置回复内容，`sleeptime设置为(1024,2048)之间`，可以根据需要修改。因为Actions一个项目限制6个小时，所以最大值不要超过2048。如果Actions显示运行超过六小时，先自行检查之前是否回复成功，若是，则把2048调整小一点。若不是，请提issues

(可选)4.下面是自己下载py文件运行时的问题

</h4>

修改以下参数，记得用''括起来

```
user=''                 用户名

password=''             密码

secret=''               谷歌身份验证器密钥
```

验证码部分根据自己选择修改参数类似上面

有能力可以自己登陆修改为使用cookies登录，就不需要验证码部分了

有bug反馈下，暂时没时间修，就放之后吧

~~**后继可能添加功能：**(已实现)~~

~~1.修改为github Actions的形式(已完成)~~

~~2.添加邮件通知功能(失败github会自己发邮件)~~

~~3.这种自动生成的api应该可以通过别的方式识别，再想办法(使用打码平台验证码识别接口)~~
