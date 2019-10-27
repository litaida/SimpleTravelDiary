myChart = echarts.init(document.getElementById('china-map'));

cache_dict = {};

option = {
    backgroundColor: '#FFFFFF',
    title: {
        text: '旅行日记',
        subtext: '',
        x:'center'
    },
    tooltip: {
        trigger: 'item',
        formatter: function (obj) {
            let province = obj.name;
            /* 请求后台数据库的对应记录, 之后记录到 cache_dict */
            if(province in cache_dict){
                return cache_dict[province]
            }else{
                cache_dict[province] = JSON.stringify({Province: obj.name});
                return cache_dict[province]
            }
        }
    },

    //配置属性
    series: [{
        name: '数据',
        type: 'map',
        mapType: 'china',
        roam: true,
        label: {
            normal: {
                show: true  //省份名称
            },
            emphasis: {
                show: false
            }
        },
    }]
};

myChart.setOption(option);
// 当鼠标移动到省份上时, 绑定模态框对象
myChart.on('mouseover', function (province_obj) {
    /* 建立模态框对象 */
	let modalBox = {};
	/* 获取模态框 */
	modalBox.modal = document.getElementById('myModal');
    /* 按下省份即为trigger */
	modalBox.triggerBtn = this._dom;
    /* 获得关闭按钮 */
	modalBox.closeBtn = document.getElementById('closeBtn');
	/* 模态框显示 */
	modalBox.show = function() {
	    /* 展示模态框时, 请求对应省份的计划数据 */
	    let province_data = JSON.parse(this.triggerBtn.textContent);
	    $.post('/travel', province_data, function (data) {
	        console.log(data);
    	    $('#content').html('<p>' + String(data['message']) + '</p>');
        });
		this.modal.style.display = 'block';
	};
	/* 模态框关闭 */
	modalBox.close = function() {
		this.modal.style.display = 'none';
	};
	/* 当用户点击模态框内容之外的区域，模态框也会关闭 */
	modalBox.outsideClick = function() {
		let modal = this.modal;
		window.onclick = function(event) {
            if(event.target === modal) {
            	modal.style.display = 'none';
            }
		}
	};
    /* 模态框初始化 */
	modalBox.init = function() {
		this.triggerBtn.onclick = function() {
            modalBox.show();
		};
		this.closeBtn.onclick = function() {
			modalBox.close();
		};
		this.outsideClick();
	};
	modalBox.init();
});
