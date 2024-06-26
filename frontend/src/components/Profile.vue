<script setup>
import { useRouter } from "vue-router";
import { useStore} from "vuex";
import SandwitchElement from "./SandwitchElement.vue";
const store = useStore();
const router = useRouter();

const user = store.state.user;
const embedLink = `${location.origin}/api/users/${user.username}/embed`;

function dispatcher(action) {
  store.dispatch(action);
  router.push('/');
}

</script>

<template>
  <h1>Your profile</h1>
  <div class="content">
    <h2>your data</h2>
    <div>
      <span>username</span>
      <span>{{ user.username }}</span>
    </div>
    <div>
      <span>embed link</span>
      <span>
        <a :href="embedLink">{{ embedLink }}</a>
        <img :src="embedLink" alt="">
      </span>
    </div>
    <div>
      <span>your sandwitches</span>
      <div>
        <span v-if="user.sandwitches.length == 0">You have no sandwitches yet</span>
        <SandwitchElement v-for="sandwitch in user.sandwitches" :sandwitch="sandwitch" v-else />
      </div>
    </div>
    <div>
      <span>your likes</span>
      <span>{{ user.sandwitches.reduce((acc, s) => acc + s.likes, 0) }}</span>
    </div>
    <div class="dangerous">
      <span>dangerous zone</span>
      <button @click="dispatcher('logout')">logout</button>
      <button @click="dispatcher('deleteUser')">delete account</button>
    </div>
  </div>
</template>

<style scoped>
div.content {
  width: 100%;

  margin-top: 70px;

  & > div {
    display: flex;
    flex-direction: column;
    margin-bottom: 1rem;
    margin-left: 5px;

    & > span {
      max-width: 500px;
    }

    & > span:nth-child(1) {
      font-weight: bold;
      letter-spacing: 1px;
    }
    & > span:nth-child(2) {
      background: #1a1a1a;
      padding: 0 8px;
      border-radius: 6px;
    }

    & > div {
      display: flex;
      flex-direction: column;
    }
  }

  & > div.dangerous {
    display: flex;
    align-items: baseline;
    gap: 10px;
    margin-top: 20px;

    & > span {
      color: red;
    }

    & > button {
      width: 300px;
      border: none;
      color: var(--primary);
      font-weight: bold;
      cursor: pointer;
      padding: 10px;

      &:nth-of-type(2) {
        background: red;
        border-radius: 6px;
        color: #D9D9D9;
        margin-top: 10px;
      }
    }
  }
}

</style>