<script setup>
import { ref } from "vue";
import { useSearchStore } from "@/stores/useSearchStore.js";
import { useRouter } from "vue-router";
import { startCrawler } from "@/api/startCrawler.js";

const router = useRouter();

const searchQuery = ref("");
const searchStore = useSearchStore();

async function performSearch() {
  searchStore.showLoading();
  searchStore.showChart();
  setTimeout(() => {
    console.log("搜索关键词:", searchQuery.value);
    searchStore.setSearchKeyword(searchQuery.value);
  }, 2000); // 搜索和加载过程
  try {
    const response = await startCrawler("/start_crawler", {
      keyword: searchQuery.value,
    });
    console.log("爬虫启动成功:", response);
    await router.push({
      name: "dashboard",
      query: { keyword: searchQuery.value },
    });
  } catch (error) {
    console.error("启动爬虫失败:", error);
  }
}
</script>

<template>
  <form class="flex">
    <label class="sr-only">Search</label>
    <div class="relative w-full">
      <div
        class="flex absolute inset-y-0 left-0 items-center pl-3 pointer-events-none"
      >
        <svg
          aria-hidden="true"
          class="w-5 h-5 text-gray-500 dark:text-gray-400"
          fill="currentColor"
          viewBox="0 0 20 20"
          xmlns="http://www.w3.org/2000/svg"
        >
          <path
            fill-rule="evenodd"
            d="M8 4a4 4 0 100 8 4 4 0 000-8zM2 8a6 6 0 1110.89 3.476l4.817 4.817a1 1 0 01-1.414 1.414l-4.816-4.816A6 6 0 012 8z"
            clip-rule="evenodd"
          ></path>
        </svg>
      </div>
      <input
        type="text"
        id="voice-search"
        class="bg-gray-50 border border-gray-300 text-gray-900 text-sm focus:ring-blue-500 focus:border-blue-500 block w-full pl-10 p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
        placeholder="请输入一些关键词"
        required=""
        v-model="searchQuery"
      />
    </div>
    <button
      type="submit"
      class="inline-flex items-center py-2.5 px-3 ml-2 text-sm font-medium text-white bg-blue-700 border border-blue-700 hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800"
      @click.prevent="performSearch"
    >
      <svg
        aria-hidden="true"
        class="mr-2 -ml-1 w-5 h-5"
        fill="none"
        stroke="currentColor"
        viewBox="0 0 24 24"
        xmlns="http://www.w3.org/2000/svg"
      >
        <path
          stroke-linecap="round"
          stroke-linejoin="round"
          stroke-width="2"
          d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"
        ></path>
      </svg>
      Search
    </button>
  </form>
</template>
