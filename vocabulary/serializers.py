from rest_framework import serializers

from vocabulary.models import Vocable, StudiedVocable, Set


class VocabularySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Vocable
        fields = ['id', 'vocab', 'translation']


class StudiedVocabSerializer(serializers.HyperlinkedModelSerializer):
    vocab = VocabularySerializer(read_only=True)
    vocable = serializers.IntegerField(write_only=True)

    class Meta:
        model = StudiedVocable
        fields = ['url', 'last_studied', 'correct_studied', 'vocab', 'vocable']

    def create(self, validated_data):
        vocab = Vocable.objects.get(id=validated_data['vocable'])
        validated_data.pop('vocable', None)
        validated_data['vocab'] = vocab
        return super().create(validated_data)


class SetSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Set
        exclude = ['vocabs']


class SetDetailSerializer(serializers.HyperlinkedModelSerializer):
    vocabs = VocabularySerializer(many=True, read_only=True)

    class Meta:
        model = Set
        fields = ['name', 'vocabs']
