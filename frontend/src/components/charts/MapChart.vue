<script setup>
import { use, registerMap } from "echarts/core";
import { ScatterChart, EffectScatterChart } from "echarts/charts";
import {
  GeoComponent,
  TitleComponent,
  LegendComponent,
  TooltipComponent
} from "echarts/components";
import { shallowRef } from "vue";
import VChart from "vue-echarts";
import getData from "@/components/charts/data/map";
import chinaMap from "@/components/charts/china.json";

use([
  ScatterChart,
  EffectScatterChart,
  GeoComponent,
  TitleComponent,
  LegendComponent,
  TooltipComponent
]);

registerMap("china", chinaMap);

const option = shallowRef(getData());
const map = shallowRef(null);
const open = shallowRef(false);

let img = null;

function convert() {
  img = {
    src: map.value.getDataURL({
      pixelRatio: window.devicePixelRatio || 1
    }),
    width: map.value.getWidth(),
    height: map.value.getHeight()
  };
  open.value = true;
}
</script>

<template>
    <v-chart
        ref="map"
        :option="option"
        autoresize
        style="background-color: #404a59"
    />
</template>