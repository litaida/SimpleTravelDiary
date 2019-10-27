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
            if (province in cache_dict) {
                return cache_dict[province]
            } else {
                $.get('/travel?Province=' + province, function (data) {
                    if(data['status'] === 200){
                        /* 查询到了 */
                        let data_dict = JSON.parse(data['message']);
                        let cache = {
                            'Province': province,
                            'Create Time': data_dict['created_at'],
                            'Note': data_dict['note']
                        };
                        cache_dict[province] = JSON.stringify(cache);
                    } else {
                        /* 没查询到 */
                        cache_dict[province] = JSON.stringify({'Province': province})
                    }
                });
                return cache_dict[province]
            }
        }
    },

    //配置属性
    series: [{
        name: '数据',
        type: 'map',
        mapType: 'china',
        roam: false,
        label: {
            normal: {
                show: true  //省份名称
            },
            emphasis: {
                show: true
            }
        },
    }]
};

myChart.setOption(option);
// 当鼠标移动到省份上时, 绑定模态框对象
myChart.on('click', function (province_obj) {
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
	    /* 展示模态框时, 展示对应省份的旅行计划, 若没有, 则展示编辑框 */
	    let province_data = JSON.parse(this.triggerBtn.textContent);
        let province = province_data['Province'];
	    let content = $('#content');
	    if ('Note' in province_data) {
            $.get('/travel?Province=' + province, function (data) {
                let msg = JSON.parse(data['message']);
                content.html(
                    '<form action="/travel" method="POST">\n' +
                    '<input type="hidden" name="province" value="' + province +'"/>\n' +
                    '<input type="hidden" name="method" value="DELETE"/>\n' +
                    '省份 <input type="text" name="province" value="' + msg['province'] +'" disabled/>\n' +
                    '旅行计划内容: <input type="text" name="note" value="' + msg['note'] +'" disabled/>\n' +
                    '创建时间: <input type="text" name="createtime" value="' + msg['created_at'] +'" disabled/>\n' +
                    '<input type="submit" value="清空" />\n' +
                    '</form>'
                );
            });
	    } else {
            content.html(
                '<form action="/travel" method="POST">\n' +
                '<input type="hidden" name="province" value="' + province +'"/>\n' +
                '省份: <input type="text" name="province_d" value="' + province +'" disabled/>\n' +
                '旅行计划内容: <input type="text" name="note" />\n' +
                '<input type="submit" value="提交" />\n' +
                '</form>'
            )
	    }
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
