<script setup>

</script>

<template>
  <h1>Recent SandWitches</h1>
  <router-link to="/create">Craft yours</router-link>
  <div class="container">
    <div class="sandwitch">
      <div class="info">
        <img src="https://via.placeholder.com/150" alt="{{ 1+1 }}"/>
        <span>{{ "Name" }}</span>
      </div>
      <div class="ingredients">
        <span>ingredients</span>
        <ul>
        </ul>
      </div>
      <div class="likes">
        <span>likes</span>
        <span>{{ 1 + 1 }}</span>
      </div>

    </div>

  </div>
</template>

<style>
main {
  display: flex;
  flex-direction: column;
  align-items: center;
}
</style>

<style scoped>
h1 {
  margin-top: -4.8rem;
  font-size: 4.2rem;
  line-height: .75;
  font-weight: 500;
  letter-spacing: -4px;
}

h1 + a {
  margin-top: 1rem;
  font-weight: bold;
  font-size: 1.4rem;

  display: inline-block;
  position: relative;
  z-index: 1;

  --back-top: 53%;
  transition: margin-top .3s, margin-bottom .3s;

  &:hover {
    margin-top: .7rem;
    margin-bottom: .35rem;
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

  margin-top: 100px;
  width: 100%;

  padding-inline: 40px;

  & > div.sandwitch {
    display: flex;
    flex-direction: row;
    justify-content: space-between;
    gap: 20px;

    background: #000;
    padding: 0 2rem;

    height: 110px;
    border-radius: 18px;

    box-sizing: border-box;

    width: 100%;

    & > div.info {
      display: flex;
      flex-direction: column;
      align-items: center;

      & > img {
        width: 120px;
        height: 120px;
        margin-top: -1.4rem;
      }

      & > span {
        color: var(--secondary);

        font-size: 1.6rem;
        font-weight: bold;
        margin-top: -1.4rem;
        margin-bottom: 1.4rem;

        display: inline-block;
      }
    }

    & > div.ingredients {
      width: 100%;

      & > span {
        color: var(--secondary);
        font-size: 1.1rem;
        font-weight: bold;

        position: relative;
        top: -.7rem;
        letter-spacing: 3px;
      }

    }

    & > div.likes {
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;

      & > span:first-of-type {
        color: var(--secondary);
        line-height: 0;

        font-size: 1.1rem;
      }

      & > span:last-of-type {

        font-size: 1.7rem;
        font-weight: bold;
      }

    }

  }
}
</style>