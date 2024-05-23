<script setup>
import { computed, onMounted, onUnmounted, reactive, ref } from "vue";
import VueApexCharts from "vue3-apexcharts";

import { useSearchStore } from "@/stores/useSearchStore";

const searchKeyword = computed(() => useSearchStore().searchKeyword);
const chartData = ref({
  series: [],
  labels: [],
  start_date: "",
  end_date: "",
});

const chart = ref(null);
const currentRange = ref("Month"); // 新添加的响应式变量，存储当前选择

let apexOptions = {
  legend: {
    show: false,
    position: "top",
    horizontalAlign: "left",
  },
  colors: ["#3C50E0", "#80CAEE"],
  chart: {
    fontFamily: "Satoshi, sans-serif",
    height: 335,
    type: "area",
    dropShadow: {
      enabled: true,
      color: "#623CEA14",
      top: 10,
      blur: 4,
      left: 0,
      opacity: 0.1,
    },

    toolbar: {
      show: false,
    },
  },
  responsive: [
    {
      breakpoint: 1024,
      options: {
        chart: {
          height: 300,
        },
      },
    },
    {
      breakpoint: 1366,
      options: {
        chart: {
          height: 350,
        },
      },
    },
  ],
  stroke: {
    width: [2, 2],
    curve: "straight",
  },

  labels: {
    show: false,
    position: "top",
  },
  grid: {
    xaxis: {
      lines: {
        show: true,
      },
    },
    yaxis: {
      lines: {
        show: true,
      },
    },
  },
  dataLabels: {
    enabled: false,
  },
  markers: {
    size: 4,
    colors: "#fff",
    strokeColors: ["#3056D3", "#80CAEE"],
    strokeWidth: 3,
    strokeOpacity: 0.9,
    strokeDashArray: 0,
    fillOpacity: 1,
    discrete: [],
    hover: {
      size: undefined,
      sizeOffset: 5,
    },
  },
  xaxis: {
    type: "category",
    categories: chartData.value.labels,
    axisBorder: {
      show: false,
    },
    axisTicks: {
      show: false,
    },
  },
  yaxis: {
    title: {
      style: {
        fontSize: "0px",
      },
    },
  },
};
let ws;

function setupWebSocket() {
  ws = new WebSocket("ws://localhost:8000/ws/tweet_trend");

  ws.onopen = function () {
    console.log("WebSocket Connection established");
    sendCurrentRange(); // 连接建立时发送当前选择
  };

  ws.onmessage = function (event) {
    // Assuming the data format is { series: [...], labels: [...] }
    // You might need to adjust this according to the actual data format
    let receiveData = JSON.parse(event.data);
    chartData.value.series = receiveData["series"];
    chartData.value.labels = receiveData["labels"];
    chartData.value.start_date = receiveData["start_date"];
    chartData.value.end_date = receiveData["end_date"];

    apexOptions = {
      ...apexOptions,
      xaxis: {
        ...apexOptions.xaxis,
        categories: chartData.value.labels,
      },
    };
  };

  // // 每隔1s时间发送关键词
  // setInterval(() => {
  //     if (ws.readyState === ws.OPEN)
  //         ws.send(searchKeyword.value);
  // }, 1000);

  ws.onerror = function (error) {
    console.log("WebSocket Error: ", error);
  };

  ws.onclose = function (event) {
    console.log("WebSocket Connection closed", event);
  };

  // 断线重连
  ws.onclose = function (event) {
    console.log("WebSocket Connection closed", event);
    setTimeout(() => {
      setupWebSocket();
    }, 3000);
  };

  setInterval(() => {
    sendCurrentRange();
  }, 3000);
}

function sendCurrentRange() {
  // 确保WebSocket连接处于开启状态
  if (ws && ws.readyState === WebSocket.OPEN) {
    // 发送当前选择和搜索关键词
    ws.send(
      JSON.stringify({
        range: currentRange.value,
        keyword: searchKeyword.value,
      })
    );
  } else {
    console.log("WebSocket Connection not established");

    // 如果WebSocket连接未建立，重新建立连接
    setupWebSocket();
    // 重新发送当前选择和搜索关键词
    sendCurrentRange();
  } 
}

// 新添加的函数，用于处理按钮点击事件
function handleRangeChange(range) {
  currentRange.value = range; // 更新当前选择
  sendCurrentRange(); // 发送新的选择到后端
}

onMounted(() => {
  setupWebSocket();
});

onUnmounted(() => {
  if (ws) {
    ws.close();
  }
});
</script>

<template>
  <div
    class="col-span-12 rounded-sm border border-stroke bg-white px-5 pt-7.5 pb-5 shadow-default dark:border-strokedark dark:bg-boxdark sm:px-7.5 xl:col-span-8"
  >
    <div
      class="flex flex-wrap items-start justify-between gap-3 sm:flex-nowrap"
    >
      <div class="flex w-full flex-wrap gap-3 sm:gap-5">
        <div class="flex min-w-47.5">
          <span
            class="mt-1 mr-2 flex h-4 w-full max-w-4 items-center justify-center rounded-full border border-primary"
          >
            <span
              class="block h-2.5 w-full max-w-2.5 rounded-full bg-primary"
            ></span>
          </span>
          <div class="w-full">
            <p class="font-semibold text-primary">正向推文</p>
            <p class="text-sm font-medium">
              {{ chartData.start_date }} - {{ chartData.end_date }}
            </p>
          </div>
        </div>
        <div class="flex min-w-47.5">
          <span
            class="mt-1 mr-2 flex h-4 w-full max-w-4 items-center justify-center rounded-full border border-secondary"
          >
            <span
              class="block h-2.5 w-full max-w-2.5 rounded-full bg-secondary"
            ></span>
          </span>
          <div class="w-full">
            <p class="font-semibold text-secondary">负面推文</p>
            <p class="text-sm font-medium">
              {{ chartData.start_date }} - {{ chartData.end_date }}
            </p>
          </div>
        </div>
      </div>
      <div class="flex w-full max-w-45 justify-end">
        <div
          class="inline-flex items-center rounded-md bg-whiter p-1.5 dark:bg-meta-4"
        >
          <button
            @click="handleRangeChange('Week')"
            :class="{ 'bg-white shadow-card': currentRange === 'Week' }"
            class="rounded py-1 px-3 text-xs font-medium text-black hover:bg-white dark:text-white dark:hover:bg-boxdark"
          >
            Week
          </button>
          <button
            @click="handleRangeChange('Month')"
            :class="{ 'bg-white shadow-card': currentRange === 'Month' }"
            class="rounded py-1 px-3 text-xs font-medium text-black hover:bg-white dark:text-white dark:hover:bg-boxdark"
          >
            Month
          </button>
        </div>
      </div>
    </div>
    <div>
      <div id="chartOne" class="-ml-5">
        <VueApexCharts
          type="area"
          height="350"
          :options="apexOptions"
          :series="chartData.series"
          ref="chart"
        />
      </div>
    </div>
  </div>
</template>
