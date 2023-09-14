<template>
	<div class="max-w-7xl mx-auto grid grid-cols-4 gap-4">
		<div class="main-center col-span-3 space-y-4">
			<div class="bg-white border border-gray-200 rounded-lg">
				<form
					method="get"
					v-on:submit.prevent="fetchSearchPosts">
					<div class="p-4 flex space-x-4">
						<input
							type="search"
							class="p-4 w-full bg-gray-100 rounded-lg"
							v-model="search_query"
							placeholder="What are you looking for?" />

						<button
							href="#"
							class="inline-block py-4 px-6 bg-purple-600 text-white rounded-lg"
							type="submit">
							search
						</button>
					</div>
				</form>
			</div>

			<div
				class="p-4 bg-white border border-gray-200 rounded-lg grid grid-cols-4 gap-4">
				<div
					class="p-4 text-center bg-gray-100 rounded-lg"
					v-for="author in authors">
					<h1 class="text-xl font-bold">{{ author.id }}</h1>
					<router-link :to="{ name: 'profile', params: { id: author.id } }">
						<img
							src="https://i.pravatar.cc/300?img=70"
							class="mb-6 rounded-full" />

						<p>
							<strong>{{ author }}</strong>
						</p>
					</router-link>

					<div class="mt-6 flex space-x-8 justify-around">
						<p class="text-xs text-gray-500">182 friends</p>
						<p class="text-xs text-gray-500">120 posts</p>
					</div>
				</div>
			</div>

			<FeedItem
				v-for="post in posts"
				:key="post.id"
				:post="post" />
		</div>

		<div class="main-right col-span-1 space-y-4">
			<PeopleYouMainKnow />
			<Trends />
		</div>
	</div>
</template>

<script>
	import PeopleYouMainKnow from '../components/PeopleYouMainKnow.vue';
	import Trends from '../components/Trends.vue';
	import FeedItem from '../components/FeedItem.vue';

	import axios from 'axios';
	export default {
		name: 'SearchView',
		components: {
			PeopleYouMainKnow,
			Trends,
			FeedItem,
		},
		setup() {
			return {};
		},
		data() {
			return {
				search_query: '',
				posts: [],
				authors: [],
			};
		},
		methods: {
			fetchSearchPosts() {
				axios
					.get('/api/v1/posts/', {
						params: {
							search_query: this.search_query,
						},
					})
					.then((response) => {
						this.posts = response.data;
						this.getAuthorsFromPosts();
					})
					.catch((error) => {
						console.log(error);
					});
			},
			getAuthorsFromPosts() {
				// Extract unique authors from the posts
				const authorMap = new Set();
				this.posts.forEach((post) => {
					authorMap.set(post.author.id, post.author);
				});

				// Convert Map values to Array
				this.authors = [...authorMap.values()];
			},
		},
	};
</script>

<style lang="postcss" scoped></style>
