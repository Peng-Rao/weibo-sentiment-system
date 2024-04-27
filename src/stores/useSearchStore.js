import { defineStore } from "pinia";
import { ref } from "vue";

export const useSearchStore = defineStore("search", () => {
  const isLoading = ref(false);
  const isChartVisible = ref(false);
  const searchKeyword = ref("");

  function showLoading() {
    isLoading.value = true;
  }

  function hideLoading() {
    isLoading.value = false;
  }

  function showChart() {
    isChartVisible.value = true;
  }

  function hideChart() {
    isChartVisible.value = false;
  }

  function setSearchKeyword(keyword) {
    searchKeyword.value = keyword;
  }

  return {
    isLoading,
    isChartVisible,
    searchKeyword,
    showLoading,
    hideLoading,
    showChart,
    hideChart,
    setSearchKeyword,
  };
});
