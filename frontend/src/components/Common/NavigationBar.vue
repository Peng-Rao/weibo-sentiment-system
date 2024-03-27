<script setup>

</script>

<template>
    <nav class="bg-gradient-to-r from-blue-500 to-blue-700 p-5 shadow-md">
      <div class="max-w-6xl mx-auto flex justify-between items-center">
        <!-- Logo -->
        <a href="#" class="flex items-center text-white">
          <svg class="h-8 w-8 mr-2" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor">
            <!-- SVG content for logo -->
          </svg>
          <span class="font-bold text-xl">Your Logo</span>
        </a>

        <!-- Primary Navigation -->
        <div class="hidden md:flex items-center space-x-4">
          <RouterLink to="" class="text-gray-100 hover:text-gray-300 transition-colors duration-300">首页</RouterLink>
          <RouterLink to="/" class="text-gray-100 hover:text-gray-300 transition-colors duration-300">关于</RouterLink>
          <RouterLink to="/" class="text-gray-100 hover:text-gray-300 transition-colors duration-300">关键词分析</RouterLink>
          <RouterLink to="/" class="text-gray-100 hover:text-gray-300 transition-colors duration-300">推文分析</RouterLink>
          <RouterLink to="/" class="text-gray-100 hover:text-gray-300 transition-colors duration-300">后台管理</RouterLink>
        </div>
      </div>
    </nav>
</template>