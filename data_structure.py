from enum import Enum
from typing import Optional, Sequence

# TODO: add Adjuncts
# TODO: add VxCs affixes

class ConcatenationType(Enum):
    TYPE_1 = "Type 1"
    TYPE_2 = "Type 2"

class Stem(Enum):
    STEM_1 = "Stem 1"
    STEM_2 = "Stem 2"
    STEM_3 = "Stem 3"

class Specification(Enum):
    BASIC = "Basic"
    CONTENTIAL = "Contential"
    CONSTITUTIVE = "Constitutive"
    OBJECTIVE = "Objective"

class Function(Enum):
    STATIC = "Static"
    DYNAMIC = "Dynamic"

class Version(Enum):
    # QUESTION: are there only two of them?
    PROCESSUAL = "Processual"
    COMPLETIVE = "Completive"

class Affiliation(Enum):
    CONSOLIDATIVE = "Consolidative"
    ASSOCIATIVE = "Associative"
    COALESCENT = "Coalescent"
    VARIATIVE = "Variative"

class Plexity(Enum):
    UNIPLEX = "Uniplex"
    DUPLEX = "Duplex"
    MULTIPLEX = "Multiplex"

class Similarity(Enum):
    SIMILAR = "Similar"
    DISSIMILAR = "Dissimilar"
    FUZZY = "Fuzzy"

class Separability(Enum):
    SEPARATE = "Separate"
    CONNECTED = "Connected"
    FUSED = "Fused"

class Configuration():
    def __init__(self, plexity: Plexity, similarity: Similarity = None, separablity: Separability = None) -> None:
        self.plexity = plexity
        if plexity == Plexity.UNIPLEX:
            self.similarity = None
            self.separablity = None
            return
        if similarity is None:
            raise ValueError("Similarity cannot be None if plexity isn't uniplex")
        if separablity is None:
            raise ValueError("Separablity cannot be None if plexity isn't uniplex")
        self.similarity = similarity
        self.separablity = separablity

class Extension(Enum):
    DELIMITIVE = "Delimitive"
    PROXIMAL = "Proximal"
    INCEPTIVE = "Inceptive"
    ATTENUATIVE = "Attenuative"
    GRADUATIVE = "Graduative"
    DEPLETIVE = "Depletive"

class Perspective(Enum):
    MONADIC = "Monadic"
    AGGLOMERATIVE = "Agglomerative"
    NOMIC = "Nomic"
    ABSTRACT = "Abstract"

class Essence(Enum):
    Normal = "Normal"
    Representative = "Representative"

class Level(Enum):
    MINIMAL = "Minimal"
    SUBEQUATIVE = "Subequative"
    INFERIOR = "Inferior"
    DEFICIENT = "Deficient"
    EQUATIVE = "Equative"
    SURPASSIVE = "Surpassive"
    SUPERLATIVE = "Superlative"
    SUPEREQUATIVE = "Superequative"
    MAXIMAL = "Maximal"

class Valence(Enum):
    MONOACTIVE = "Monoactive"
    PARALLEL = "Parallel"
    COROLLARY = "Corollary"
    RECIPROCAL = "Reciprocal"
    COMPLEMENTARY = "Complementary"
    NONRELATIONAL = "Nonrelational"
    DUPLICATIVE = "Duplicative"
    DEMONSTRATIVE = "Demonstrative"
    PARTICIPATIVE = "Participative"

class Phase(Enum):
    CONTEXTUAL = "Contextual"
    PUNCTUAL = "Punctual"
    ITERATIVE = "Iterative"
    REPETITIVE = "Repetitive"
    INTERMITTENT = "Intermittent"
    RECURRENT = "Recurrent"
    FREQUENTATIVE = "Frequentative"
    FRAGMENTATIVE = "Fragmentative"
    FLUCTUATIVE = "Fluctuative"

class Effect(Enum):
    # QUESTION: are there any explanation to those 1-3 values?
    BENEFICIAL_1 = "Beneficial 1"
    BENEFICIAL_2 = "Beneficial 2"
    BENEFICIAL_3 = "Beneficial 3"
    BENEFICIAL_SELF = "Beneficial to formative itself"
    UNKNOWN = "Unknown"
    DETRIMENTAL_SELF = "Detrimental to formative itself"
    DETRIMENTAL_3 = "Detrimental 3"
    DETRIMENTAL_2 = "Detrimental 2"
    DETRIMENTAL_1 = "Detrimental 1"

class Aspect(Enum):
    RETROSPECTIVE = "Retrospective"
    RESUMPTIVE = "Resumptive"
    PREEMPTIVE = "Preemptive"
    DISCLUSIVE = "Disclusive"
    PROSPECTIVE = "Prospective"
    CESSATIVE = "Cessative"
    CLIMACTIC = "Climactic"
    CONCLUSIVE = "Conclusive"
    HABITUAL = "Habitual"
    PAUSAL = "Pausal"
    DILATORY = "Dilatory"
    CULMINATIVE = "Culminative"
    PROGRESSIVE = "Progressive"
    REGRESSIVE = "Regressive"
    TEMPORARY = "Temporary"
    INTERMEDIATIVE = "Intermediative"
    IMMINENT = "Imminent"
    PRECLUSIVE = "Preclusive"
    EXPENDITIVE = "Expenditive"
    TARDATIVE = "Tardative"
    PRECESSIVE = "Precessive"
    CONTINUATIVE = "Continuative"
    LIMITATIVE = "Limitative"
    TRANSITIONAL = "Transitional"
    REGULATIVE = "Regulative"
    INCESSATIVE = "Incessative"
    EXPEDITIVE = "Expeditive"
    INTERCOMMUTATIVE = "Intercommutative"
    SUMMATIVE = "Summative"
    EXPERIENTIAL = "Experiential"
    PROTRACTIVE = "Protractive"
    MOTIVE = "Motive"
    ANTICIPATORY = "Anticipatory"
    INTERRUPTIVE = "Interruptive"
    PREPARATORY = "Preparatory"
    SEQUENTIAL = "Sequential"

class Mood(Enum):
    FACTUAL = "Factual"
    SUBJUNCTIVE = "Subjunctive"
    ASSUMPTIVE = "Assumptive"
    SPECULATIVE = "Speculative"
    COUNTERFACTIVE = "Counterfactive"
    LISTEN = "Listen"
    HYPOTHETICAL = "Hypothetical"
    IMPLICATIVE = "Implicative"
    ASCRIPTIVE = "Ascriptive"

class CaseScope(Enum):
    NATURAL = "Natural"
    ANTECEDENT = "Antecedent"
    SUBALTERN = "Subaltern"
    QUALIFIER = "Qualifier"
    PRECEDENT = "Precedent"
    SUCCESSIVE = "Successive"

class Context(Enum):
    EXISTENTIAL = "Existential"
    FUNCTIONAL = "Functional"
    REPRESENTATIONAL = "Representational"
    AMALGAMATIVE = "Amalgamative"

class Case(Enum):
    THEMATIC = "Thematic"
    INSTRUMENTAL = "Instrumental"
    ABSOLUTIVE = "Absolutive"
    AFFECTIVE = "Affective"
    STIMULATIVE = "Stimulative"
    EFFECTUATIVE = "Effectuative"
    ERGATIVE = "Ergative"
    DATIVE = "Dative"
    INDUCIVE = "Inducive"
    POSSESSIVE = "Possessive"
    PROPRIETIVE = "Proprietive"
    GENITIVE = "Genitive"
    ATTRIBUTIVE = "Attributive"
    PRODUCTIVE = "Productive"
    INTERPRETATIVE = "Interpretative"
    ORIGINATIVE = "Originative"
    INTERDEPENDENT = "Interdependent"
    PARTITIVE = "Partitive"
    APPLICATIVE = "Applicative"
    PURPOSIVE = "Purposive"
    TRANSMISSIVE = "Transmissive"
    DEFERENTIAL = "Deferential"
    CONTRASTIVE = "Contrastive"
    TRANSPOSITIVE = "Transpositive"
    COMMUTATIVE = "Commutative"
    COMPARATIVE = "Comparative"
    CONSIDERATIVE = "Considerative"
    FUNCTIVE = "Functive"
    TRANSFORMATIVE = "Transformative"
    CLASSIFICATIVE = "Classificative"
    RESULTATIVE = "Resultative"
    CONSUMPTIVE = "Consumptive"
    CONCESSIVE = "Concessive"
    AVERSIVE = "Aversive"
    CONVERSIVE = "Conversive"
    SITUATIVE = "Situative"
    PERTINENTIAL = "Pertinential"
    DESCRIPTIVE = "Descriptive"
    CORRELATIVE = "Correlative"
    COMPOSITIVE = "Compositive"
    COMITATIVE = "Comitative"
    UTILITATIVE = "Utilitative"
    PREDICATIVE = "Predicative"
    RELATIVE = "Relative"
    ACTIVATIVE = "Activative"
    ASSIMILATIVE = "Assimilative"
    ESSIVE = "Essive"
    TERMINATIVE = "Terminative"
    SELECTIVE = "Selective"
    CONFORMATIVE = "Conformative"
    DEPENDENT = "Dependent"
    VOCATIVE = "Vocative"
    LOCATIVE = "Locative"
    ATTENDANT = "Attendant"
    ALLATIVE = "Allative"
    ABLATIVE = "Ablative"
    ORIENTATIVE = "Orientative"
    INTERRELATIVE = "Interrelative"
    INTRATIVE = "Intrative"
    NAVIGATIVE = "Navigative"
    CONCURSIVE = "Concursive"
    ASSESSIVE = "Assessive"
    PERIODIC = "Periodic"
    PROLAPSIVE = "Prolapsive"
    PRECURSIVE = "Precursive"
    POSTCURSIVE = "Postcursive"
    ELAPSIVE = "Elapsive"
    PROLIMITIVE = "Prolimitive"

class Illocution(Enum):
    ASSERTIVE = "Assertive"
    DIRECTIVE = "Directive"
    DECLARATIVE = "Declarative"
    INTERROGATIVE = "Interrogative"
    VERIFICATIVE = "Verificative"
    ADMONITIVE = "Admonitive"
    POTENTIATIVE = "Potentiative"
    HORTATIVE = "Hortative"
    CONJECTURAL = "Conjectural"

class Validation(Enum):
    OBSERVATIONAL = "Observational"
    RECOLLECTIVE = "Recollective"
    PURPORTIVE = "Purportive"
    REPORTIVE = "Reportive"
    UNSPECIFIED = "Unspecified"
    IMAGINARY = "Imaginary"
    CONVENTIONAL = "Conventional"
    INTUITIVE = "Intuitive"
    INFERENTIAL = "Inferential"

class Bias(Enum):
    ACCIDENTAL = "Accidental"
    ARCHETYPAL = "Archetypal"
    ADMISSIVE = "Admissive"
    ANNUNCIATIVE = "Annunciative"
    ANTICIPATIVE = "Anticipative"
    APPROBATIVE = "Approbative"
    APPREHENSIVE = "Apprehensive"
    ARBITRARY = "Arbitrary"
    ATTENTIVE = "Attentive"
    COMEDIC = "Comedic"
    CONTENSIVE = "Contensive"
    COINCIDENTAL = "Coincidental"
    CORRUPTIVE = "Corruptive"
    CORRECTIVE = "Corrective"
    CONTEMPTIVE = "Contemptive"
    CONTEMPLATIVE = "Contemplative"
    DISCONCERTIVE = "Disconcertive"
    DEJECTIVE = "Dejective"
    DESPERATIVE = "Desperative"
    DIFFIDENT = "Diffident"
    DISMISSIVE = "Dismissive"
    DELECTATIVE = "Delectative"
    DOLOROUS = "Dolorous"
    DISAPPROBATIVE = "Disapprobative"
    DERISIVE = "Derisive"
    DUBITATIVE = "Dubitative"
    EUPHORIC = "Euphoric"
    EUPHEMISTIC = "Euphemistic"
    EXASPERATIVE = "Exasperative"
    EXIGENT = "Exigent"
    EXPERIENTIAL = "Experiential"
    FORTUITOUS = "Fortuitous"
    FASCINATIVE = "Fascinative"
    GRATIFICATIVE = "Gratificative"
    INDIGNATIVE = "Indignative"
    INFATUATIVE = "Infatuative"
    IMPLICATIVE = "Implicative"
    IMPATIENT = "Impatient"
    IRONIC = "Ironic"
    INSIPID = "Insipid"
    INVIDIOUS = "Invidious"
    MANDATORY = "Mandatory"
    OPTIMAL = "Optimal"
    PESSIMISTIC = "Pessimistic"
    PROPITIOUS = "Propitious"
    PERPLEXIVE = "Perplexive"
    PROPOSITIVE = "Propositive"
    PROSAIC = "Prosaic"
    PRESUMPTIVE = "Presumptive"
    REACTIVE = "Reactive"
    REFLECTIVE = "Reflective"
    RENUNCIATIVE = "Renunciative"
    REPULSIVE = "Repulsive"
    REVELATIVE = "Revelative"
    SATIATIVE = "Satiative"
    SUGGESTIVE = "Suggestive"
    SKEPTICAL = "Skeptical"
    SOLICITATIVE = "Solicitative"
    STUPEFACTIVE = "Stupefactive"
    TREPIDATIVE = "Trepidative"
    VEXATIVE = "Vexative"

class Relation(Enum):
    FRAMED = "Framed"
    UNFRAMED = "Unframed"


class Formative():
    pass

class StandAloneFormative(Formative):
    # QUESTION: where is an Expectation in docs?
    # QUESTION: what's the slot for the bias?
    def __init__(self, 
        root: str,
        specification: Specification, 
        function: Function,
        context: Context,
        configuration: Configuration,
        affiliation: Affiliation,
        extension: Extension,
        perspective: Perspective,
        essence: Essence,
        relation: Relation,
        stem: Optional[Stem] = None,
        version: Optional[Version] = None,
        valence: Optional[Valence] = None,
        phase: Optional[Phase] = None,
        effect: Optional[Effect] = None,
        level: Optional[Level] = None,
        aspect: Optional[Aspect] = None,
        mood: Optional[Mood] = None,
        case_scope: Optional[CaseScope] = None,
        cases: Optional[Sequence[Case]] = None,
        validation: Optional[Validation] = None,
        illocution: Optional[Illocution] = None,
        bias: Optional[Bias] = None
    ) -> None:
        self.root = root
        self.stem = stem
        self.specification = specification
        self.function = function
        self.version = version
        self.configuration = configuration
        self.affiliation = affiliation
        self.extension = extension
        self.perspective = perspective
        self.essence = essence
        self.context = context
        self.mood = mood
        self.case_scope = case_scope
        self.valence = valence
        self.phase = phase
        self.effect = effect
        self.level = level
        self.aspect = aspect
        self.case = cases
        self.validation = validation
        self.illocution = illocution
        self.bias = bias
        self.relation = relation

class ConcatenatedChainFormative(Formative):
    def __init__(self, formatives: Sequence[StandAloneFormative], concatenation: ConcatenationType) -> None:
        if len(formatives) < 2:
            raise ValueError("Not enough elements in the sequence of formatives")
        self.formatives = formatives
        self.concatenation = concatenation

class Sentence:
    def __init__(self, formatives: Sequence[Formative]) -> None:
        self.formatives = formatives
