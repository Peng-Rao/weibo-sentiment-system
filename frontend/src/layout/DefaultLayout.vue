<script setup>
import HeaderArea from "@/components/Header/HeaderArea.vue";
import Footer from "@/components/Footer/Footer.vue";
</script>

<template>
    <!-- ===== Page Wrapper Start ===== -->
    <div class="flex h-screen overflow-hidden">
        <!-- ===== Sidebar Start ===== -->
        <!-- ===== Sidebar End ===== -->

        <!-- ===== Content Area Start ===== -->
        <div class="relative flex flex-1 flex-col overflow-y-auto overflow-x-hidden">
            <!-- ===== Header Start ===== -->
            <header-area/>
            <!-- ===== Header End ===== -->

            <!-- ===== Main Content Start ===== -->
            <main>
                <div class="mx-auto max-w-screen-2xl p-4 md:p-6 2xl:p-10">
                    <slot></slot>
                </div>
            </main>
            <!-- ===== Main Content End ===== -->
            <Footer></Footer>
        </div>
    </div>
    <!-- ===== Page Wrapper End ===== -->
</template>

<style scoped>

</style>