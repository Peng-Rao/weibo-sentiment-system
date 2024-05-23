<script setup>
import { ref } from "vue";
import { getPrediction } from "@/api/prediction";
import DefaultLayout from "@/layout/DefaultLayout.vue";
import VueWordCloud from "vuewordcloud";
import VueApexCharts from "vue3-apexcharts";

const inputData = ref("");
const chartData = ref({
  series: [],
  labels: [],
});
const positiveProbability = ref(0);
const negativeProbability = ref(0);
const wordCloudData = ref([
  ["restaurant", 19],
  ["horror", 3],
  ["fantasy", 7],
  ["adventure", 3],
]);
let apexOptions = {
  chart: {
    type: "donut",
    width: 380,
  },
  colors: ["#3C50E0", "#6577F3", "#8FD0EF", "#0FADCF"],
  labels: [],
  legend: {
    show: false,
    position: "bottom",
  },
  plotOptions: {
    pie: {
      donut: {
        size: "65%",
        background: "transparent",
      },
    },
  },
  dataLabels: {
    enabled: false,
  },
  responsive: [
    {
      breakpoint: 640,
      options: {
        chart: {
          width: 200,
        },
      },
    },
  ],
};

const handleSubmit = async () => {
  if (!inputData.value.trim()) return; // 确保输入不为空
  try {
    let responseData = await getPrediction("/predict", {
      text: inputData.value,
    });
    let probabilities = responseData["probabilities"];
    chartData.value.series = [
      probabilities["positive"],
      probabilities["negative"],
    ];
    positiveProbability.value = probabilities["positive"];
    negativeProbability.value = probabilities["negative"];
    // 清空输入框
    apexOptions = {
      ...apexOptions,
      series: chartData.value.series,
      labels: ["正面概率", "反面概率"],
    };
    wordCloudData.value = responseData["word_freq"];
  } catch (error) {
    console.error("提交失败:", error);
  }
  console.log("提交成功:", inputData.value);
};
</script>

<template>
  <default-layout>
    <label
      for="message"
      class="block mb-2 text-sm font-medium text-gray-900 dark:text-white"
      >推文</label
    >
    <textarea
      rows="6"
      placeholder="请输入需要分析的推文"
      class="w-full rounded-lg border-[1.5px] text-black border-stroke bg-transparent py-3 px-5 font-normal outline-none transition focus:border-primary active:border-primary disabled:cursor-default disabled:bg-whiter dark:text-white dark:border-form-strokedark dark:bg-form-input dark:focus:border-primary"
      v-model="inputData"
    ></textarea>
    <button
      @click="handleSubmit"
      class="block w-full p-3 mt-4 text-sm font-medium text-white bg-blue-500 rounded-lg shadow-md hover:bg-blue-600 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:ring-offset-2"
    >
      Get Prediction
    </button>
    <div
      class="mt-4 grid grid-cols-12 gap-4 md:mt-6 md:gap-6 2xl:mt-7.5 2xl:gap-7.5"
    >
      <div
        class="col-span-12 rounded-sm border border-stroke bg-white px-5 pt-7.5 pb-5 shadow-default dark:border-strokedark dark:bg-boxdark sm:px-7.5 xl:col-span-5"
      >
        <div class="mb-3 justify-between gap-4 sm:flex">
          <div>
            <h4 class="text-xl font-bold text-black dark:text-white">
              情感分类
            </h4>
          </div>
        </div>
        <div class="mb-2">
          <div id="chartThree" class="mx-auto flex justify-center">
            <VueApexCharts
              type="donut"
              width="340"
              :options="apexOptions"
              :series="chartData['series']"
              ref="chart"
            />
          </div>
        </div>
        <div class="-mx-8 flex flex-wrap items-center justify-center gap-y-3">
          <div class="w-full px-8 sm:w-1/2">
            <div class="flex w-full items-center">
              <span
                class="mr-2 block h-3 w-full max-w-3 rounded-full bg-primary"
              ></span>
              <p
                class="flex w-full justify-between text-sm font-medium text-black dark:text-white"
              >
                <span> 正面概率 </span>
                <span> {{ positiveProbability }} </span>
              </p>
            </div>
          </div>
          <div class="w-full px-8 sm:w-1/2">
            <div class="flex w-full items-center">
              <span
                class="mr-2 block h-3 w-full max-w-3 rounded-full bg-[#4f5ba7]"
              ></span>
              <p
                class="flex w-full justify-between text-sm font-medium text-black dark:text-white"
              >
                <span> 反面概率 </span>
                <span> {{ negativeProbability }} </span>
              </p>
            </div>
          </div>
        </div>
      </div>
      <!-- ====== Chart Three End -->

      <!-- ====== Map One Start -->
      <!--      <MapOne />-->
      <div
        class="col-span-12 rounded-sm border border-stroke bg-white py-6 px-7.5 shadow-default dark:border-strokedark dark:bg-boxdark xl:col-span-7"
      >
        <vue-word-cloud
          :words="wordCloudData"
          :color="
            ([, weight]) =>
              weight > 10 ? 'DeepPink' : weight > 5 ? 'RoyalBlue' : 'Indigo'
          "
          font-family="Finger Paint"
          animation-easing="ease-in"
          enter-animation="zoom"
        />
      </div>
    </div>
  </default-layout>
</template>
