<script setup>
import {use, registerTheme} from "echarts/core";
import {BarChart} from "echarts/charts";
import {GridComponent, DatasetComponent} from "echarts/components";
import {shallowRef, onBeforeUnmount} from "vue";
import VChart from "vue-echarts";
import getData from "@/components/Charts/data/bar";
import theme from "@/components/Charts/theme.json";

use([BarChart, DatasetComponent, GridComponent]);
registerTheme("ovilia-green", theme);

const seconds = shallowRef(0);
const loading = shallowRef(false);
const loadingOptions = {
    text: "Loading…",
    color: "#4ea397",
    maskColor: "rgba(255, 255, 255, 0.4)"
};
const option = shallowRef(getData());

let timer = null;

onBeforeUnmount(() => {
    clearInterval(timer);
});

function tick() {
    seconds.value--;

    if (seconds.value === 0) {
        clearInterval(timer);
        loading.value = false;
        option.value = getData();
    }
}

function refresh() {
    // simulating async data from server
    seconds.value = 3;
    loading.value = true;

    timer = setInterval(tick, 1000);
}
</script>

<template>
    <div>
        <v-chart
            :option="option"
            theme="ovilia-green"
            autoresize
            :loading="loading"
            :loadingOptions="loadingOptions"
            style="height: 100vh"
        ></v-chart>
        <button @click="refresh">Refresh</button>
        <p v-if="loading">Refreshing in {{ seconds }} seconds...</p>
    </div>
</template>