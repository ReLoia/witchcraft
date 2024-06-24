<script setup>
import Sandwitch from './SandwitchText.vue'
import '@jamescoyle/svg-icon'
import {mdiCartPlus, mdiDelete, mdiPlusCircle} from "@mdi/js";
import {onMounted, reactive, ref} from 'vue'

// INGREDIENTS

const isIngredientOpen = ref(false)

const currentIngredient = reactive({
  name: "",
  amount: 1,
  file: null,
  thickness: 1,
  size: {
    width: 1,
    height: 1
  }
})

const ingredients = reactive([
  {
    name: "Ingredient",
    amount: 1,
    src: "https://via.placeholder.com/150",
    thickness: 1,
    size: {
      width: 1,
      height: 1
    }
  }
])

// TODO: make ingredients get loaded from backend

function addIngredient(ingredient) {
  console.log("mamtm", ingredient)

  if (ingredient.name === "")
    return;

  if (ingredient.amount === 0)
    return;

  if (ingredient.size.width === 0 || ingredient.size.height === 0)
    return;

  if (ingredient.thickness === 0)
    return;

  ingredients.push({...ingredient, src: URL.createObjectURL(ingredient.file)})
}

function removeIngredient(element) {
  const index = ingredients.indexOf(element)
  if (index > -1) {
    ingredients.splice(index, 1)
  }
}

// GENRES

const isGenreOpen = ref(false)

// TODO: move ingredients to backend and make it load from backend
// TODO: also make ingredients editable from users (creating new ones)
const possibleGenres = reactive([
  "magical", "psychical", "metallic", "organic", "plastic", "wooden", "glass", "stone", "liquid", "gaseous", "solid", "hot", "cold", "frozen", "burning", "rotten", "fresh", "artificial", "natural", "synthetic", "alien", "human", "animal", "plant", "mineral", "chemical", "biological", "technological", "spiritual", "emotional", "physical", "mental", "abstract", "concrete", "tasteful", "tasteless", "smelly", "smell-less",
])

const sandWitch = reactive({
  name: "",
  description: "",
  genre: ["magical"],
  ingredients: ingredients
})

function addGenre(genre) {
  sandWitch.genre.push(genre)
}

function removeGenre(genre) {
  const index = sandWitch.genre.indexOf(genre)
  if (index > -1) {
    sandWitch.genre.splice(index, 1)
  }
}

// on mount add event listener to overlay
onMounted(() => {
  const overlay = document.querySelector('.overlay');

  overlay.addEventListener('click', () => {
    isIngredientOpen.value = false
  })
})

</script>

<template>
  <h1>Craft your
    <Sandwitch/>
  </h1>
  <div class="content" :class="(isIngredientOpen || isGenreOpen) ? 'open-overlay' : ''">
    <div class="ingredients">
      <span>ingredients</span>
      <ul>
        <li v-for="ingredient in ingredients">
          <template v-for="i in ingredient.amount">
            <button @click="removeIngredient(ingredient)">
              <svg-icon type="mdi" :path="mdiDelete"/>
            </button>
            <img :src="ingredient.src" alt="Could not load image"/>
            <span>
              {{ ingredient.name }}
            </span>
          </template>
        </li>
      </ul>
      <button @click="isIngredientOpen = true">
        <svg-icon type="mdi" :path="mdiCartPlus"/>
      </button>
    </div>
    <div class="add-ingredient" :class="isIngredientOpen ? 'open' : ''">
      <span><b>Add</b> an ingredient</span>
      <div class="ingredient_img">
        <label for="ingredient_img"></label>
        <input type="file" name="ingredient_img" id="ingredient_img" accept="image/*" v-on:change="currentIngredient.file = $event.target.files[0]">
      </div>
      <div class="text_input">
<!--        what is it <b>called</b>? -->
        <label for="ingredient_name">what is it <b>called</b>?</label>
        <input type="text" v-model="currentIngredient.name">
      </div>
<!--      how <b>many</b> of it? -->
      <div class="text_input">
        <label for="ingredient_amount">how <b>many</b> of it?</label>
        <input type="number" v-model="currentIngredient.amount">
      </div>

<!--      how <b>big</b> is it?, two inputs in one row -->
      <div class="text_input">
        <label for="ingredient_size">how <b>big</b> is it?</label>
        <div class="row">
          <input type="number" v-model="currentIngredient.size.width">
          <input type="number" v-model="currentIngredient.size.height">
        </div>
      </div>
<!--      how <b>thick</b> is it? >-->
      <div class="text_input">
        <label for="ingredient_thickness">how <b>thick</b> is it?</label>
        <input type="number" v-model="currentIngredient.thickness">
      </div>

<!-- TODO:
All those are instances of div.text_input, the first with a single input, the second with two inputs (40% the size of the first) and the last a signle input with 40% the size of the first
          also, all these will have a label with the text written in the comment above. Also those will change the variable ingredient to the value of the input
 -->

      <button @click="addIngredient(currentIngredient); isIngredientOpen=false">
        <b>Add</b> it to the ingredients
      </button>
    </div>
    <div class="craft">
      <div class="input">
        <label for="">name your
          <Sandwitch/>
        </label>
        <input type="text"/>
      </div>
      <div class="input">
        <label for="">describe your
          <Sandwitch/>
        </label>
        <textarea name="" id="" cols="30" rows="10"></textarea>
      </div>
      <div class="input">
        <label for="">what kind of
          <Sandwitch/>
          did you make</label>
        <div class="genres">
          <div class="genre" v-for="genre in sandWitch.genre">
            <span>{{ genre }}</span>
            <button @click="removeGenre(genre)">
              <svg-icon type="mdi" :path="mdiDelete"/>
            </button>
          </div>

          <button @click="isGenreOpen = true">
            <svg-icon type="mdi" :path="mdiPlusCircle"/>
          </button>
        </div>
      </div>
      
      <div class="buttons">
        <button>Craft it!</button>
        <router-link class="button" to="/">Cancel</router-link>
      </div>
    </div>
  </div>
  <div class="overlay"></div>
</template>

<!--<script>-->
<!--const overlay = document.querySelector('.overlay');-->

<!--overlay.addEventListener('click', () => {-->
<!--  this.isIngredientOpen.value = false-->
<!--})-->
<!--</script>-->

<style scoped>
h1 {
  margin-top: -4.8rem;
  font-size: 4.3rem;
  line-height: .75;
  font-weight: 400;
  letter-spacing: -4px;
}



div.content {
  display: flex;
  flex-direction: row;
  justify-content: space-between;

  width: 100%;
  margin-top: 100px;

  gap: 100px;
  position: relative;

  & > .add-ingredient,
  & > .ingredients {
    width: 280px;
    border-radius: 24px;

    background: #000;
    box-shadow: -10px 14px 0 rgba(217, 217, 217, 0.8);
    min-height: 600px;

    position: relative;

    & > span {
      color: var(--secondary);
      font-size: 1.2rem;
      font-weight: bold;

      position: relative;
      top: -1rem;
      letter-spacing: 2px;

      left: 25%;
      transform: translateX(-50%);
    }

    & > ul {
      display: flex;
      flex-direction: column;
      align-items: center;
      padding: 0;

      max-height: 560px;

      & > li {
        display: flex;
        flex-direction: column;
        align-items: center;
        padding: 10px;
        position: relative;

        & > img {
          width: 100px;
          height: 100px;
        }

        & > span {
          color: var(--primary);
          font-size: .9rem;
          font-weight: bold;
          position: relative;
          top: -.7rem;
        }

        & > button {
          opacity: 0;
          pointer-events: none;

          color: var(--primary);
          scale: .8;

          cursor: pointer;

          background: none;
          border: none;
          padding: 0;

          position: absolute;
          top: -10px;
          right: -10px;

          transition: all .3s;

          background: var(--background);
          width: 34px;
          height: 34px;
          border-radius: 50%;
          line-height: 44px;
        }

        &:hover > button {
          pointer-events: all;
          opacity: 1;
        }
      }
    }

    & > button {
      color: var(--secondary);
      scale: 1.4;

      position: absolute;
      bottom: 14px;
      right: 14px;

      border: none;
      padding: 0;

      width: 32px;
      height: 32px;
      line-height: 46px;
    }

  }

  & > .add-ingredient {
    display: none;
  }
  & > .add-ingredient.open {
    position: absolute;

    left: 300px;
    z-index: 20;

    display: flex;
    flex-direction: column;

    box-sizing: border-box;

    padding: 14px 10px;

    gap: 5px;

    & > span {
      font-weight: 500;
      color: #FFFFFF;
      left: 10px;
      margin-top: -1.7rem;
      top: unset;
      transform: unset;

      & > b {
        color: var(--secondary);
      }
    }

    & > .ingredient_img {
      margin-top: 20px;
      width: 140px;
      height: 140px;
      border-radius: 12px;

      background: #D9D9D9;

      & > input {
        display: none;
      }

      & > label {
        display: block;
        width: 100%;
        height: 100%;

        cursor: pointer;
      }
    }

    & > .text_input {
      display: flex;
      flex-direction: column;

      & > label {
        font-size: 1rem;
        letter-spacing: 2px;
        margin-left: 20px;

        & > b {
          color: var(--secondary);
        }
      }

      input {
        background: #D9D9D9;
        color: var(--background);
        border: none;
        padding: 4px 8px;

        box-shadow: -6px 8px 0 #000;

        width: 100%;
        border-radius: 6px;
        font-size: .9rem;
        font-weight: bold;
        letter-spacing: 2px;

        box-sizing: border-box;
      }

      & > .row {
        display: flex;
        flex-direction: row;
        justify-content: space-between;

        & > input {
          width: 40%;
        }
      }

    }

    & > button {
      all: unset;

      margin-top: auto;
      cursor: pointer;
      background: #D9D9D9;
      border-radius: 8px;
      color: #000;

      font-size: 1.1rem;

      text-align: center;

      & > b {
        color: var(--secondary);
      }
    }
  }

  & > .craft {
    width: 90%;
    max-width: 760px;

    margin-top: -27px;

    display: flex;
    flex-direction: column;

    & > .input {
      display: flex;
      flex-direction: column;
      gap: 10px;

      & > label {
        font-size: 1.3rem;
        letter-spacing: 2px;
        margin-bottom: -13px;
        margin-left: 20px;
      }

      & > input,
      & > textarea,
      & > div {
        background: #D9D9D9;
        color: var(--background);
        border: none;
        padding: 4px 8px;

        box-shadow: -6px 8px 0 #000;

        width: 100%;
        border-radius: 12px;
        font-size: .9rem;
        font-weight: bold;
        letter-spacing: 2px;
        margin-bottom: 20px;

        resize: none;
        min-height: 34px;

        box-sizing: border-box;
      }

      & > div.genres {
        display: flex;
        flex-direction: row;
        align-items: center;
        padding-block: 0;

        gap: 30px;

        padding-right: 100px;

        position: relative;

        & > div.genre {
          font-size: .76rem;
          letter-spacing: 0;
          font-weight: bold;

          display: flex;
          flex-direction: row;
          align-items: center;


          & > span {
            background: var(--background);
            color: #D9D9D9;
            padding: 0 4px;
            border-radius: 6px;
          }

          & > button {
            background: var(--background);
            color: red;
            border: none;
            padding: 0;

            margin-left: -8px;

            width: 34px;
            height: 34px;
            line-height: 48px;
            border-radius: 10px;

            scale: .54;
          }
        }

        & > button {
          background: var(--background);
          border: none;
          padding: 0 10px;
          border-radius: 6px;
          height: 16px;

          position: absolute;
          right: 10px;

          & > svg-icon {
            color: var(--secondary);;

            position: relative;
            top: -4px;
          }

        }
      }


    }

    & > div.buttons {
      display: flex;
      flex-direction: row;

      gap: 40px;
      margin-top: auto;
      align-self: flex-end;

      & > button,
      & > .button{
        background: #D9D9D9;
        color: var(--background);
        border: none;
        padding: 4px 8px;
        text-align: center;

        height: 34px;
        line-height: 26px;

        --bsh-x: -6px;
        --bsh-y: 8px;
        --bsh-c: #000;

        box-shadow: var(--bsh-x) var(--bsh-y) 0 var(--bsh-c);

        min-width: 200px;

        border-radius: 12px;
        font-size: .9rem;
        font-weight: bold;
        letter-spacing: 2px;

        box-sizing: border-box;

        transition: all .2s;

        &:nth-child(1) {
          color: var(--secondary);
          --bsh-c: var(--secondary);
        }

        &:nth-child(2) {
          color: red;
          --bsh-c: red;
        }

        &:hover {
          --bsh-x: -10px;
          --bsh-y: 14px;
        }

      }
    }
  }

}

div.content.open-overlay + .overlay {
  width: 100%;
  height: 100%;

  position: absolute;
  top: 0;
  left: 0;

  background: rgba(0, 0, 0, .5);
  backdrop-filter: blur(1px);
  z-index: 1;
}

</style>