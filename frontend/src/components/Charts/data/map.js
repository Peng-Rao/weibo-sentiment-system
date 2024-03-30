const data = [
    {
        name: "北京",
        value: 54,
    },
    {
        name: "南海诸岛",
        value: 0,
    },
    {
        name: "天津",
        value: 13,
    },
    {
        name: "上海",
        value: 40,
    },
    {
        name: "重庆",
        value: 75,
    },
    {
        name: "河北",
        value: 13,
    },
    {
        name: "河南",
        value: 83,
    },
    {
        name: "云南",
        value: 11,
    },
    {
        name: "辽宁",
        value: 19,
    },
    {
        name: "黑龙江",
        value: 15,
    },
    {
        name: "湖南",
        value: 69,
    },
    {
        name: "安徽",
        value: 60,
    },
    {
        name: "山东",
        value: 39,
    },
    {
        name: "新疆",
        value: 4,
    },
    {
        name: "江苏",
        value: 31,
    },
    {
        name: "浙江",
        value: 104,
    },
    {
        name: "江西",
        value: 36,
    },
    {
        name: "湖北",
        value: 1052,
    },
    {
        name: "广西",
        value: 33,
    },
    {
        name: "甘肃",
        value: 7,
    },
    {
        name: "山西",
        value: 9,
    },
    {
        name: "内蒙古",
        value: 7,
    },
    {
        name: "陕西",
        value: 22,
    },
    {
        name: "吉林",
        value: 4,
    },
    {
        name: "福建",
        value: 18,
    },
    {
        name: "贵州",
        value: 5,
    },
    {
        name: "广东",
        value: 98,
    },
    {
        name: "青海",
        value: 1,
    },
    {
        name: "西藏",
        value: 0,
    },
    {
        name: "四川",
        value: 44,
    },
    {
        name: "宁夏",
        value: 4,
    },
    {
        name: "海南",
        value: 22,
    },
    {
        name: "台湾",
        value: 3,
    },
    {
        name: "香港",
        value: 5,
    },
    {
        name: "澳门",
        value: 5,
    },
];

export default function getData() {
    return {
        textStyle: {
            fontFamily: 'Inter, "Helvetica Neue", Arial, sans-serif',
            fontWeight: 300
        },
        title: {
            text: "全国评论分布",
            left: "center",
            textStyle: {
                color: "#fff",
                fontSize: 30,
            },
            subtextStyle: {
                fontSize: 20,
            },
        },
        tooltip: {
            trigger: "item"
        },
        // 热力地图
        visualMap: {
            min: 0,
            max: 1000,
            left: 240,
            textStyle: {
                color: "#fff",
            },
            pieces: [
                {
                    gt: 100,
                    label: "> 100 人",
                    color: "#7f1100",
                },
                {
                    gte: 10,
                    lte: 100,
                    label: "10 - 100 人",
                    color: "#ff5428",
                },
                {
                    gte: 1,
                    lt: 10,
                    label: "1 - 9 人",
                    color: "#ff8c71",
                },
                {
                    value: 0,
                    label: "无",
                    color: "#ffd768",
                },
            ],
        },

        series: [
            {
                name: "评论数数量",
                data: data,
                type: "map",
                map: "china",
                zoom: 1.2,
                aspectScale: 0.75,
                label: {
                    formatter: "{b}",
                    position: "center",
                    show: true
                },
                itemStyle: {
                    color: "#f4e925",
                    shadowBlur: 10,
                    shadowColor: "#333"
                },
            },
        ],
    };
}