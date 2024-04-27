<script setup>
import { registerTheme, use } from "echarts/core";
import { BarChart } from "echarts/charts";
import { DatasetComponent, GridComponent } from "echarts/components";
import { onBeforeUnmount, onMounted, ref } from "vue";
import VChart from "vue-echarts";
import theme from "@/components/Charts/theme.json";
import { CanvasRenderer } from "echarts/renderers";

use([BarChart, DatasetComponent, GridComponent, CanvasRenderer]);
registerTheme("ovilia-green", theme);

// const seconds = shallowRef(0);
// const loading = shallowRef(false);
// const loadingOptions = {
//     text: "Loading…",
//     color: "#4ea397",
//     maskColor: "rgba(255, 255, 255, 0.4)"
// };
const option = ref({});
let ws = null;

onMounted(() => {
  ws = new WebSocket("ws://localhost:8000/ws/bar");

  ws.onmessage = (event) => {
    option.value = JSON.parse(event.data); // Update the chart data
  };

  ws.onopen = () => console.log("WebSocket connection opened.");
  ws.onerror = (error) => console.error("WebSocket error:", error);
  ws.onclose = () => console.log("WebSocket connection closed.");
});

onBeforeUnmount(() => {
  if (ws.value) ws.value.close();
});
</script>

<template>
  <div
    class="col-span-12 rounded-sm border border-stroke bg-white p-7.5 shadow-default dark:border-strokedark dark:bg-boxdark xl:col-span-4"
  >
    <div class="mb-4 justify-between gap-4 sm:flex">
      <div>
        <h4 class="text-xl font-bold text-black dark:text-white">
          Profit this week
        </h4>
      </div>
      <!-- 选择器和其他控件可在此处添加，如第一段代码中所示 -->
    </div>
    <v-chart
      :option="option"
      theme="ovilia-green"
      autoresize
      class="bg-transparent"
    >
    </v-chart>
  </div>
</template>
