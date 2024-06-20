<script setup>
</script>

<template>
  <div class="title">
    <h2>witch</h2>
    <h2>CRAFT</h2>
    <div id="underline">

    </div>
  </div>
</template>

<script>
  export default {
    name: 'App',
    data() {
      return {
        h2Color: '#fff'
      }
    },
    methods: {
      randomColor() {
        let color = '#';
        for (let i = 0; i < 6; i++) {
          color += Math.floor(Math.random() * 16).toString(16);
        }
        return color;
      }
    },
  };

  setInterval(() => {
    this.h2Color = this.randomColor();
  }, 1000);
</script>

<style scoped>
  .title {
    text-align: center;
    font-size: 4rem;
    line-height: .75;
    width: fit-content;
    transform: rotateZ(350deg);

    & > h2 {
      margin: 0;
      padding: 0;

      &:nth-child(2) {
        color: v-bind(h2Color);
      }
    }

    & > div#underline {
      width: 100%;
      height: 14px;
      background-color: black;
      margin: 10px auto;
      border-radius: 24px;

    }
  }
</style>
