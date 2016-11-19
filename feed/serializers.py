from rest_framework import serializers
from workflow.models import Program, Sector, ProjectType, Office, SiteProfile, Country, ProjectComplete, \
    ProjectAgreement, Stakeholder, Capacity, Evaluate, ProfileType, \
    Province, District, AdminLevelThree, Village, StakeholderType, Contact, Documentation, LoggedUser
from indicators.models import Indicator, ReportingFrequency, TolaUser, IndicatorType, Objective, DisaggregationType, \
    Level, ExternalService, ExternalServiceRecord, StrategicObjective, CollectedData, TolaTable, DisaggregationValue
from django.contrib.auth.models import User


class UserSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'is_staff')


class ProgramSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Program
        fields = '__all__'


class SectorSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Sector
        fields = '__all__'


class ProjectTypeSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = ProjectType
        fields = '__all__'


class OfficeSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Office
        fields = '__all__'


class SiteProfileSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = SiteProfile
        fields = '__all__'


class CompleteSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = ProjectComplete
        fields = '__all__'


class AgreementSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = ProjectAgreement
        fields=(
                'id',
                'program',
                'date_of_request',
                'project_name',
                'project_type',
                'project_activity',
                'project_description',
                'site',
                'activity_code',
                'office',
                'sector',
                'project_design',
                'account_code',
                'lin_code',
                'stakeholder',
                'effect_or_impact',
                'expected_start_date',
                'expected_end_date',
                'expected_duration',
                'total_estimated_budget',
                'mc_estimated_budget',
                'local_total_estimated_budget',
                'local_mc_estimated_budget',
                'exchange_rate',
                'exchange_rate_date',
                'estimation_date',
                'estimated_by',
                'estimated_by_date',
                'checked_by',
                'checked_by_date',
                'reviewed_by',
                'reviewed_by_date',
                'finance_reviewed_by',
                'finance_reviewed_by_date',
                'me_reviewed_by',
                'me_reviewed_by_date',
                'capacity',
                'evaluate',
                'approval',
                'approved_by',
                'approved_by_date',
                'approval_submitted_by',
                'approval_remarks',
                'justification_background',
                'risks_assumptions',
                'justification_description_community_selection',
                'description_of_project_activities',
                'description_of_government_involvement',
                'description_of_community_involvement',
                'community_project_description')


class CountrySerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Country
        fields = '__all__'


class IndicatorSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Indicator
        fields = '__all__'


class ReportingFrequencySerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = ReportingFrequency
        fields = '__all__'


class TolaUserSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = TolaUser
        fields = ('url', 'name','country', 'countries')

class IndicatorTypeSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = IndicatorType
        fields = '__all__'


class ObjectiveSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Objective
        fields = '__all__'


class DisaggregationTypeSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = DisaggregationType
        fields = '__all__'


class LevelSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Level
        fields = '__all__'


class StakeholderSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Stakeholder
        fields = '__all__'


class ExternalServiceSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = ExternalService
        fields = '__all__'


class ExternalServiceRecordSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = ExternalServiceRecord
        fields = '__all__'


class StrategicObjectiveSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = StrategicObjective
        fields = '__all__'

class StakeholderTypeSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = StakeholderType
        fields = '__all__'


class CapacitySerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Capacity
        fields = '__all__'


class EvaluateSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Evaluate
        fields = '__all__'


class ProfileTypeSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = ProfileType
        fields = '__all__'


class ProvinceSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Province
        fields = '__all__'


class DistrictSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = District
        fields = '__all__'


class AdminLevelThreeSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = AdminLevelThree
        fields = '__all__'


class VillageSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Village
        fields = '__all__'


class ContactSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Contact
        fields = '__all__'


class DocumentationSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Documentation
        fields = '__all__'


class CollectedDataSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = CollectedData
        fields = '__all__'


class TolaTableSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = TolaTable
        fields = '__all__'


class DisaggregationValueSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = DisaggregationValue

class LoggedUserSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = LoggedUser
		fields = ('username', 'country', 'email')
