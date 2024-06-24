<script setup>
import { ref } from 'vue';

const craftedSandwitches = ref(0);

// TODO: make craftedSandwitches be loaded from the server

</script>

<template>
  <header>
    <router-link to="/" class="title">
      <span>witch</span>
      <span>CRAFT</span>
      <div id="underline"></div>
    </router-link>
    <div class="stats">
      <div class="digits">
<!--        <span>0</span>-->
<!--        <span>0</span>-->
<!--        <span>0</span>-->
<!--        <span>0</span>-->
        <span v-for="digit in craftedSandwitches.toString().padStart(4, '0').split('')" :key="digit">{{ digit }}</span>
      </div>
      <p>
        <span>sandwitches</span> <span>crafted</span>
      </p>
    </div>
  </header>
  <main>
    <RouterView />
  </main>
</template>

<script>

// each frame get window.mouse and rotate title and stats based on the mouse direction
function rotateTitleAndStats() {
  const title = document.querySelector("header .title");
  const stats = document.querySelector("header .stats");

  /**
   * @type {*|{left: boolean, x: number, y: number, right: boolean}}
   */
  const mouse = window.mouse;

  if (mouse) {
    const angleTitleMouse = Math.atan2(mouse.y - title.offsetTop, mouse.x - title.offsetLeft) * 180 / Math.PI;
    const angleStatsMouse = Math.atan2(mouse.y - stats.offsetTop, mouse.x - stats.offsetLeft) * 180 / Math.PI;

    title.style.rotate = `${Math.max(Math.min(angleTitleMouse - 80, 20), -20)}deg`;
    stats.style.rotate = `${Math.max(Math.min(angleStatsMouse - 80, 20), -20)}deg`;
  }

  requestAnimationFrame(rotateTitleAndStats);
}
requestAnimationFrame(rotateTitleAndStats);

</script>

<style scoped>
  main {
    display: flex;
    flex-direction: column;
    align-items: center;
  }

  header {
    display: flex;
    flex-direction: row;
    align-items: center;
    justify-content: space-between;

    padding-top: 20px;
    height: 90px;

    & > .title {
      text-align: center;
      font-size: 3.6rem;
      line-height: .75;
      width: fit-content;

      transform: scale(.6) rotate(-3deg);

      display: flex;
      flex-direction: column;
      letter-spacing: -4px;

      color: inherit;

      transition: rotate .1s .01s;

      & > span {
        margin: 0;
        padding: 0;
        font-size: .9em;


        &:nth-child(2) {
          font-size: 1.1em;
          font-weight: bold;
          color: var(--primary);
        }
      }

      & > div#underline {
        width: 110%;
        height: 8px;

        transform: translate(-4%, 0);

        background-color: #D9D9D9;
        margin: 10px auto;
        border-radius: 24px;

        transition: 1s cubic-bezier(0.19, 1, 0.22, 1) ;
      }

      &:hover > div#underline {
        background-color: var(--secondary);
      }
    }

    & > .stats {
      display: flex;
      flex-direction: column;
      align-items: center;

      transform: rotate(3deg);

      transition: rotate .1s .01s;

      & > .digits {
        display: flex;
        flex-direction: row;
        align-items: center;
        justify-content: center;

        & > span {
          font-size: 3rem;
          line-height: .75;
          font-weight: bold;
        }
      }

      & > p {
        font-size: .85em;
        color: #D9D9D9;
      }
    }
  }

</style>
