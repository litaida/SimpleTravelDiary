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
                console.log('写入 cache_dict');
                cache_dict[province] = 'Province<br>' + obj.name;
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
myChart.on('click', function (params) {
    refresh(this)
});

function refresh(){
    alert('You Clicked')
}
