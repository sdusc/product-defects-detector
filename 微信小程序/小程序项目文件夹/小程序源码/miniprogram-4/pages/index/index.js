
//index.js  
//获取应用实例  
var app = getApp()  
Page({  
  data: {  //下面的数据是设置全局变量
    tempFilePaths: '',
    result:'',
    pre_time:'',
    detect_time:'',
    cloudPath:''  
  },  
  onLoad: function () {  
  },  
  chooseimage: function () {  
    var _this = this;  //通过this这个实例来调用接口
    var random_1 = Math.floor(Math.random() * 10);//生成0-10的数字,随机确定百位
    var random_2 = Math.floor(Math.random() * 100);//生成0-100的数字,随机确定十位和个位

    var random_1_1 = Math.floor(Math.random() * 10);//生成0-10的数字,随机确定百位
    var random_2_2 = Math.floor(Math.random() * 100);//生成0-100的数字,随机确定十位和个位



    var random_time = random_1*100+random_2;//生成一个三位整数
    var random_time_pre = random_1_1*100+random_2_2;//生成一个三位整数
    var random_3 = Math.floor(Math.random() + 0.5);//小于一和大于一的概率都是0.5
    var random_4 = Math.floor(Math.random() + 0.5);//小于一和大于一的概率都是0.5
    var random_result = '未知'
    var random_type = '未知类别'
    if (random_3>=1)
      random_result = '有缺陷';
    else
      random_result = '无缺陷';
    
    if (random_4>=1)
      random_type = '随机类别一';
    else
      random_type = '随即类别二';

    wx.chooseMedia({  
      count: 1, //指定最多上传图片的大小
      mediaType: ['image'],//指定上传的文件类型为图片类型
      sourceType: ['album', 'camera'], // 可以指定来源是相册还是相机，默认二者都有  
      sizeType: ['original'],//这是原图的意思，另外有一个压缩的选项，我们默认原图，方便检测
      camera: 'back',//如果要拍照的话，默认设置为后置摄像头
      success: function (res) {  
        // 返回选定照片的本地文件路径列表,tempFiles[i]里面包含某张图片信息,如下 
        // 3个值：fileType:"image";size:大小;tempFilePath:路径
        // [i]可以选择第几张图片,如果想要发送所有图片的话使用for循环即可
        // 但是为了方便开发,我决定选择一次只能选择一张图片来进行,多图片交给WEB端
        console.log(res.tempFiles)//console.log()函数是在控制台进行打印,res是返回值,tempFiles是本地文件信息，包括路径，大小，多少张之类的信息
        console.log(res.tempFiles[0].tempFilePath)//第一张图片的本地路径（因为可以选择多张，所以是数组类型）
        _this.setData({  
          tempFilePaths:res.tempFiles[0].tempFilePath//这里的setData方法是设置前端的绑定值，与VUE语法类似，先空着，拿到数据后再让前端显示出来  
        })  

        wx.request({
          url: 'https://www.escook.cn/api/post',//这是微信的REQUEST接口
          // url:'http://103.46.128.53/',
          method: "POST",
          data: {//额外携带的数据
              result: random_result,
              pre_time: random_time_pre,
              detect_time:random_time
          },
          success: (res) => {   //成功之后执行的方法
              console.log(res.data)
              _this.setData({  
                result:res.data.data.result,
                pre_time:res.data.data.pre_time, 
                detect_time:res.data.data.detect_time
              })  
          }
          })
      }  
    })  
  },
  
  chooseimage_cloud: function () {  
    var fileid_id = ''
    var _this = this;  
    wx.chooseMedia({  
      count: 1, //指定最多上传图片的大小
      mediaType: ['image'],
      sourceType: ['album', 'camera'], // 可以指定来源是相册还是相机，默认二者都有  
      sizeType: ['original'],
      camera: 'back',
      success: function (res) {  
        const tempFilePaths = res.tempFiles
        console.log('===================tempFiles = ',tempFilePaths)
        const filePath = String(res.tempFiles[0].tempFilePath)
        const cloudPath = 'WX.image'

        _this.setData({  
          //这里设置在前端展示的内容,第一个是是否有缺陷,第二个是处理速度  
          tempFilePaths:res.tempFiles[0].tempFilePath 
        })  

        wx.cloud.uploadFile({
          cloudPath:cloudPath,    //这里的cloudPath是云端服务器的id，通过id来传到对应的服务器上
          // url: 'http://example.weixin.qq.com/upload', //仅为示例，非真实的接口地址
          // url:'https://t54897w513.goho.co/',
          filePath: filePath,
          name: 'JPG',
          formData:{
            'user': 'WECHAT-YZQ'    //额外携带的数据
          },
          success: function(res){   //上传成功后执行的代码
            console.log('OK')
            console.log('云端ID为:'+res.fileID)
            var data = JSON.parse(res.data)
            console.log(data)
            //do something
            fileid_id = res.fileID
            console.log()
          },
          complete: function (res) {  //无论成功与否，都会执行的方法
            console.log('方法完成了,自动执行现在的部分');
            console.log('这是在打印fileid之前的句子')
            console.log(res.fileID)
            console.log(fileid_id)
            wx.cloud.getTempFileURL({   //微信小程序的接口，用于获取下载链接
              fileList: [{
                fileID: res.fileID,     //通过文件id来查找文件
                maxAge: 60 * 60, // one hour，也就是这个文件的存活时间，超过这个时间就不要了
              }]
            }).then(res => {
              // get temp file URL
              console.log('现在进入到了指定位置')
              console.log(res.fileList)
              var URL = res.fileList[0].tempFileURL
              wx.request({
                // url: 'https://www.escook.cn/api/post',
                url:'https://t54897w513.goho.co',
                method: "POST",
                data: {
                  downloadURL:URL
                },
                success: (res) => {
                    console.log(res)
                    console.log('成功了!')
                    _this.setData({  
                      //这里设置在前端展示的内容,第一个是是否有缺陷,第二个是处理速度  
                      // cloudPath:'https://t54897w513.goho.co/image',
                      result: res.data.msg,
                      pre_time: res.data.time[0],
                      detect_time:res.data.time[1]
                    })

                }
                })

            }).catch(error => {
              console.log('发生未知错误')
              console.log(error)
              // handle error
            })
    
          }
        })

      }
    })
  },

      // 发起POST请求
      postInfo() {
        var _this = this;  
        var random_1 = Math.floor(Math.random() * 10);//生成0-10的数字,随机确定百位
        var random_2 = Math.floor(Math.random() * 100);//生成0-100的数字,随机确定十位和个位
        var random_time = random_1*100+random_2;
        var random_3 = Math.floor(Math.random() + 0.5);//小于一和大于一的概率都是0.5
        var random_4 = Math.floor(Math.random() + 0.5);//小于一和大于一的概率都是0.5
        var random_result = '未知'
        var random_type = '未知类别'
        if (random_3>=1)
          random_result = '有缺陷';
        else
          random_result = '无缺陷';
        
        if (random_4>=1)
          random_type = '随机类别一';
        else
          random_type = '随即类别二';




        wx.request({
        url: 'https://www.escook.cn/api/post',
        // url:'https://t54897w513.goho.co/',
        method: "POST",
        data: {
            result: random_result,
            time: random_time,
            type: random_type
        },
        success: (res) => {
            console.log(res)
            console.log(res.data)

            // console.log(res.data.data.age)
            // console.log(res.data.age)
            // console.log(res.data.time)
        }
        })
    }

})  



// // index.js
// // 获取应用实例
// const app = getApp()

// Page({
//   data: {
//     motto: 'Hello World',
//     userInfo: {},
//     hasUserInfo: false,
//     canIUse: wx.canIUse('button.open-type.getUserInfo'),
//     canIUseGetUserProfile: false,
//     canIUseOpenData: wx.canIUse('open-data.type.userAvatarUrl') && wx.canIUse('open-data.type.userNickName') // 如需尝试获取用户信息可改为false
//   },
//   // 事件处理函数
//   bindViewTap() {
//     wx.navigateTo({
//       url: '../logs/logs'
//     })
//   },
//   onLoad() {
//     if (wx.getUserProfile) {
//       this.setData({
//         canIUseGetUserProfile: true
//       })
//     }
//   },
//   getUserProfile(e) {
//     // 推荐使用wx.getUserProfile获取用户信息，开发者每次通过该接口获取用户个人信息均需用户确认，开发者妥善保管用户快速填写的头像昵称，避免重复弹窗
//     wx.getUserProfile({
//       desc: '展示用户信息', // 声明获取用户个人信息后的用途，后续会展示在弹窗中，请谨慎填写
//       success: (res) => {
//         console.log(res)
//         this.setData({
//           userInfo: res.userInfo,
//           hasUserInfo: true
//         })
//       }
//     })
//   },
//   getUserInfo(e) {
//     // 不推荐使用getUserInfo获取用户信息，预计自2021年4月13日起，getUserInfo将不再弹出弹窗，并直接返回匿名的用户个人信息
//     console.log(e)
//     this.setData({
//       userInfo: e.detail.userInfo,
//       hasUserInfo: true
//     })
//   }
// })
