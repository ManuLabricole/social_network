<template>
	<div class="main-right col-span-1 space-y-4">
		<PeopleYouMayKnow :profile="profile" />
		<Trends :profile="profile" />
	</div>
</template>

<script>
	import PeopleYouMayKnow from '../../components/feed/PeopleYouMayKnow.vue';
	import Trends from '../../components/feed/Trends.vue';
	export default {
		components: {
			PeopleYouMayKnow,
			Trends,
		},
		props: {
			profile: {
				type: Object,
				required: true,
			},
		},
	};
</script>
