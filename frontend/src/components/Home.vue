<script setup>
import {onMounted, reactive, ref} from 'vue'
import { useStore} from "vuex";
import SandwitchText from "./SandwitchText.vue";
import SandwitchElement from "./SandwitchElement.vue";
const store = useStore();

// TODO: load sandwitches from the server
const sandwitches = ref([]);

onMounted(async () => {
  const response = await fetch('/api/sandwitches');
  if (response.ok) {
    sandwitches.value = await response.json();
  }
})

</script>

<template>
  <h1>Recent <SandwitchText/>es</h1>
  <router-link to="/craft">Craft yours</router-link>
  <div class="container">
    <div class="loading" v-if="sandwitches.length == 0">
      <span>There are no sandwitches yet</span>
    </div>
    <SandwitchElement v-for="sandwitch in sandwitches" v-else :sandwitch="sandwitch" />
  </div>
</template>

<style scoped>

h1 + a {
  margin-top: 1rem;
  font-weight: bold;
  font-size: 1.4rem;

  display: inline-block;
  position: relative;
  z-index: 1;

  --back-top: 53%;
  transition: margin-top .3s, margin-bottom .3s, top .3s;

  top: 0;

  &:hover {
    top: -.3rem;
    --back-top: 65%;
  }

  &:after {
    content: "";
    display: block;
    width: 80%;
    height: 40%;

    transition: top .3s;

    position: absolute;
    top: var(--back-top);
    left: 50%;
    transform: translateX(-50%);
    z-index: -1;

    border-radius: 50px;

    background: black;
  }
}

div.container {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;

  margin-top: 70px;
  width: 100%;

  gap: 40px;
  padding-inline: 40px;

}
</style>