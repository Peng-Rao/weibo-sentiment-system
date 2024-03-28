<script setup>
import {registerTheme, use} from "echarts/core";
import {BarChart} from "echarts/charts";
import {DatasetComponent, GridComponent} from "echarts/components";
import {onBeforeUnmount, onMounted, ref} from "vue";
import VChart from "vue-echarts";
import theme from "@/components/charts/theme.json";

use([BarChart, DatasetComponent, GridComponent]);
registerTheme("ovilia-green", theme);

// const seconds = shallowRef(0);
// const loading = shallowRef(false);
// const loadingOptions = {
//     text: "Loading…",
//     color: "#4ea397",
//     maskColor: "rgba(255, 255, 255, 0.4)"
// };
const option = ref({});
let ws = null

onMounted(() => {
    ws = new WebSocket('ws://localhost:8000/bar');

    ws.onmessage = (event) => {
        option.value = JSON.parse(event.data); // Update the chart data
    };

    ws.onopen = () => console.log('WebSocket connection opened.');
    ws.onerror = (error) => console.error('WebSocket error:', error);
    ws.onclose = () => console.log('WebSocket connection closed.');
});

onBeforeUnmount(() => {
    if (ws.value) ws.value.close();
});
</script>

<template>
    <div>
        <v-chart
            :option="option"
            theme="ovilia-green"
            autoresize
            style="height: 100vh"
        ></v-chart>
    </div>
</template>