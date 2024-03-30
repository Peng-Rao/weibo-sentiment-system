<script setup>
import {use, registerMap} from "echarts/core";
import {ScatterChart, EffectScatterChart, MapChart} from "echarts/charts";
import {
    GeoComponent,
    TitleComponent,
    LegendComponent,
    TooltipComponent, VisualMapComponent
} from "echarts/components";
import {computed, onBeforeUnmount, onMounted, ref} from "vue";
import VChart from "vue-echarts";
import getData from "@/components/Charts/data/map";
import chinaMap from "@/components/Charts/china.json";
import {CanvasRenderer} from "echarts/renderers";

use([
    ScatterChart,
    EffectScatterChart,
    GeoComponent,
    TitleComponent,
    LegendComponent,
    TooltipComponent,
    CanvasRenderer,
    VisualMapComponent,
    MapChart
]);

registerMap("china", chinaMap);

const map = ref(null);

const data = getData();

const option = ref({
    textStyle: {
        fontFamily: 'Inter, "Helvetica Neue", Arial, sans-serif',
        fontWeight: 300
    },
    title: {
        text: "",
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
    series: [
        {
            name: "评论数数量",
            data: null,
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
    ]
});
let ws = null

import {useSearchStore} from "@/stores/useSearchStore";

const searchKeyword = computed(() => useSearchStore().searchKeyword);

onMounted(() => {
    ws = new WebSocket('ws://localhost:8000/ws/province-count');

    ws.onmessage = (event) => {
        const newData = JSON.parse(event.data);
        option.value = {...option.value, series: [{...option.value.series[0], data: newData}]};
    };

    // 发送关键词
    ws.onopen = () => {
        ws.send(searchKeyword.value);
        console.log('WebSocket connection opened.');
    }

    // 每隔1s时间发送关键词
    setInterval(() => {
        if (ws.readyState === ws.OPEN)
            ws.send(searchKeyword.value);
    }, 1000);

    ws.onerror = (error) => console.error('WebSocket error:', error);
    ws.onclose = () => console.log('WebSocket connection closed.');
});

onBeforeUnmount(() => {
    if (ws.value) ws.value.close();
});
</script>

<template>
    <v-chart
        ref="map"
        :option="option"
        autoresize
        style="background-color: #404a59"
    />
</template>