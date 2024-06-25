<script setup>
import {onMounted, ref} from 'vue';
import { useStore } from 'vuex';
const store = useStore();

const loginFormOpen = ref(false);

const craftedSandwitches = ref(0);

// TODO: make craftedSandwitches be loaded from the server

// TODO: store login in global scope
const user = store.state.user;
console.log("user", user)

onMounted(() => {
  const overlay = document.querySelector('.overlay');

  overlay.addEventListener('click', e => {
    if (e.target === overlay) loginFormOpen.value = false;
  })
})

</script>

<template>
  <header>
    <router-link to="/" class="title">
      <span>witch</span>
      <span>CRAFT</span>
      <div id="underline"></div>
    </router-link>
    <router-link to="/profile" v-if="user.name" class="stats">
      <span>your</span>
      <span>profile</span>
    </router-link>
    <button v-else class="stats" @click="loginFormOpen = true">
      <span>login</span>
      <span>to craft</span>
    </button>
  </header>
  <main>
    <RouterView />
  </main>
  <div class="overlay" :class="{ open: loginFormOpen }">
    <div class="login-form">
      <h1>Login</h1>
      <div>
        <label for="username">Username</label>
        <input type="text" id="username" />
      </div>
      <div>
        <label for="password">Password</label>
        <input type="password" id="password" />
      </div>
      <button>Login</button>
    </div>

  </div>
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

<style>
main > h1 {
  margin-top: -4.8rem;
  font-size: 4.3rem;
  line-height: .75;
  font-weight: 400;
  letter-spacing: -4px;
}
</style>

<style scoped>
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

      padding: 0;
      background: none;

      transform: rotate(3deg);
      transition: rotate .1s .01s;

      & > span {
        font-size: 2rem;
        line-height: .9;
        font-weight: bold;
      }

      &:after {
        content: "";
        display: block;
        width: 90%;
        height: 5px;
        background-color: #D9D9D9;
        margin-top: 5px;
        border-radius: 5px;

        transition: 1s cubic-bezier(0.19, 1, 0.22, 1) ;
      }

      &:hover {
        border: none;
        color: var(--secondary);
        &:after {
          background-color: var(--secondary);
        }
      }

    }
  }

  main {
    display: flex;
    flex-direction: column;
    align-items: center;
  }

  .overlay {
    display: none;

    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background-color: rgba(0, 0, 0, .5);
    justify-content: center;
    align-items: center;
    z-index: 1000;

    cursor: pointer;

    &.open {
      display: flex;
    }

    & > .login-form {
      display: flex;
      flex-direction: column;
      align-items: center;
      gap: 20px;

      width: 100%;
      height: 100%;
      max-height: 400px;
      max-width: min(380px, 97%);

      border-radius: 12px;

      background: var(--background);

      padding: 20px 30px;

      z-index: 1;
      pointer-events: all;

      & > div {
        width: 100%;

        & > label {
          display: block;
          font-size: .9rem;
          font-weight: bold;
          margin-left: 10px;
          margin-bottom: -10px;
        }

        & > input {
          width: 100%;
          padding: 10px;
          border: none;
          border-radius: 8px;
          box-sizing: border-box;

          margin-top: 10px;
        }
      }

      & > button {
        width: 100%;
        padding: 10px;
        border: none;
        border-radius: 8px;

        margin-top: auto;

        background: var(--secondary);
        color: #D9D9D9;

        font-size: 1.1rem;
        font-weight: bold;

        cursor: pointer;
      }
    }
  }
</style>
