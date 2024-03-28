<script setup>
import {ref, onMounted} from "vue";
import { getPrediction } from "@/api/prediction";

const data = ref(null);
const inputData = ref('');

const handleSubmit = async () => {
  if (!inputData.value.trim()) return; // 确保输入不为空
  try {
    const response = await getPrediction('/predict', { text: inputData.value });
    console.log('提交成功:', response);
    // 清空输入框或进行其他逻辑处理...
  } catch (error) {
    console.error('提交失败:', error);
  }
};

</script>

<template>
<label for="message" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Your message</label>
<textarea id="message" rows="4" class="block p-2.5 w-full text-sm text-gray-900 bg-gray-50 rounded-lg border border-gray-300 focus:ring-blue-500 focus:border-blue-500 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" placeholder="Write your thoughts here..." v-model="inputData"></textarea>
<button @click="handleSubmit" class="block w-full p-3 mt-4 text-sm font-medium text-white bg-blue-500 rounded-lg shadow-md hover:bg-blue-600 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:ring-offset-2">Get Prediction</button>
</template>