<template>
	<div class="max-w-7xl mx-auto grid grid-cols-4 gap-4">
		<div class="main-left col-span-1">
			<div class="p-4 bg-white border border-gray-200 text-center rounded-lg">
				<img
					src="https://i.pravatar.cc/300?img=70"
					class="mb-6 rounded-full" />

				<p><strong>Code With Stein</strong></p>
				<div class="mt-6 flex space-x-8 justify-around">
					<p class="text-xs text-gray-500">182 friends</p>
					<p class="text-xs text-gray-500">120 posts</p>
				</div>
			</div>
		</div>
		<div class="main-center col-span-2 space-y-4">
			<div class="bg-white border border-gray-200 rounded-lg">
				<form
					class="space-y-1"
					method="post"
					v-on:submit.prevent="createPost">
					<div class="p-4 pb-1">
						<input
							type="text"
							class="p-4 w-50 h-4 bg-gray-100 rounded-full"
							v-model="postTitle"
							placeholder="add a title"
							maxlength="50" />
					</div>
					<div
						v-if="titleError"
						class="m-4 p-4 pb-1 pt-1 gap-4 text-gray-300 bg-red-500 rounded-lg">
						{{ titleError }}
					</div>
					<div class="p-4 pb-1 pt-1">
						<textarea
							class="p-4 w-full bg-gray-100 rounded-lg"
							v-model="postBody"
							placeholder="What are you thinking about?"></textarea>
					</div>
					<div class="p-4 border-t border-gray-100 flex justify-between">
						<a
							href="#"
							class="inline-block py-4 px-6 bg-gray-600 text-white rounded-lg"
							>Attach image</a
						>
						<button
							href="#"
							class="inline-block py-4 px-6 bg-purple-600 text-white rounded-lg">
							Post
						</button>
					</div>
				</form>
			</div>
			<FeedItem
				v-for="post in posts"
				v-bind:key="post.id"
				v-bind:post="post" />
		</div>
		<div class="main-right col-span-1 space-y-4">
			<PeopleYouMayKnow />
			<Trends />
		</div>
	</div>
</template>

<script>
	import PeopleYouMayKnow from '@/components/feed/PeopleYouMayKnow.vue';
	import Trends from '@/components/feed/Trends.vue';
	import FeedItem from '@/components/feed/FeedItem.vue';
	import axios from 'axios';

	export default {
		name: 'FeedView',
		components: {
			PeopleYouMayKnow,
			Trends,
			FeedItem,
		},
		data() {
			return {
				posts: [],
				postBody: '',
				postTitle: '',
				titleError: '',
			};
		},
		mounted() {
			this.getFeed();
		},
		methods: {
			getFeed() {
				axios
					.get('/api/v1/posts')
					.then((response) => {
						this.posts = response.data;
					})
					.catch((error) => {
						console.error(error);
						console.warn('Error getting feed');
					});
			},
			createPost() {
				axios
					.post('/api/v1/posts/', {
						title: this.postTitle,
						body: this.postBody,
					})
					.then((response) => {
						console.log(response);
						this.body = '';
						this.posts.unshift(response.data);
					})
					.catch((error) => {
						console.error('ERROR', error);
						this.titleError = error.response.data.title[0];
					});
			},
		},
	};
</script>
